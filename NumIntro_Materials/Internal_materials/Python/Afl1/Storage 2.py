# import numpy as np
#
# from numpy.linalg import matrix_power
# from scipy.linalg import expm
#
# def expomat2(A, x, N=10**2, eps=10**(-8)):
#     # Implementation af matrix expotential ud fra (ligning (3)).
#     # Input er en kvadratisk matrix A, en skalar x, og evt. ændrede beføjelser af N og eps.
#     # Programmet stopper efter N trin, eller gennem brug af ligning (4) kriteriet
#     # - Her er det Sseqtest-variablen skal være > 1 - eps.
#     # Vi bemærker, at vi har undgået .append-løsninger, og har inkluderet alt det tunge maskineri indenfor én for-loop.
#
#     if np.shape(A)[0] != np.shape(A)[1]:  # Simpel "Passer dimensionerne (er A kvadratisk?)"-test
#         raise AttributeError("A skal være en kvadratisk matrix")
#
#     I = np.identity(np.shape(A)[0]).astype(np.int64)
#     A = A.astype(np.float64)  # Evt. konvertering af A til en matrix med elementer af datatype
#     # 'float 64 bit'
#
#     # Da vi har at a_ii <= - sum_{{j=1}_j \ne i}^n{aij}, og a_{i\ne j}>=0 vil max af (-1)*diagonalelementerne
#     # være max af (-1)*alle elementer i rækken, hvorfor den inderste np.max-funktion er skrevet som den er.
#     # - Man kunne dog sagtens forestille sig at det ville være komputationelt billigere at bede Python specifikt om at
#     # kigge langs diagonalen - Her er altså en videreudviklingsmulighed
#
#     #Bemærk også at vi har brug for to max funktionen her, idet np.max(-A, axis = 1) giver en
#     # vektor med max-værdien for hver række, og det er denne vi skal have max af i definitionen af eta.
#
#     eta = np.max(np.max(-A, axis=1))
#
#     P = (I + ((1/eta) * A)).astype(np.float64)
#     Sseqtest = 0
#     Sseq = 0
#
#     for n in range(0, N + 1):
#         #Udregning af følgen bag vores teststørrelse.
#         seqtest = (x**n * eta**n / np.math.factorial(n)) * np.exp(- eta * x)
#         #Printfunktion til at udforske tælleren af seqtest
#         print('x**{} = {},\n eta**{} = {},\n x**{}*eta**{} = {}'.format(n,x**n, n, eta**n, n, n, x**n * eta**n))
#
#         Sseqtest += seqtest
#         print('\nseqtest_{} = {}.  Sseqtest_{} = {}'.format(n, seqtest, n, Sseqtest))
#         if Sseqtest <= 1 - eps:
#             Sseq += seqtest * matrix_power(P, n)
#             print('\nSseq_{} =\n{}'.format(n, Sseq))
#         else:
#             print('\n1 - eps = {}.\nVi stopper ved trin {} da Sseqtest_{} = {} > 1 - eps.'.format(1 - eps, n - 1, n, Sseqtest))
#             print('Sseq_{} =\n{}'.format(n - 1, Sseq))  # Vi skal have n-1 her, da n-1 fortsat er mindre end eps fra exp(Ax) i inf-norm
#             break
#     return Sseq
#
#     # -----
#
# A = np.array([[-5, 2, 3],[2, -6, 4],[4, 5, -9]])
# A_20 = A * 1/20
#
#
# qq = 11
# expomat2(A, x = qq, N=10**3)
# print('expm\n', expm(A*qq))
#
# #Lav graf over nedenstående
# # 1 = 29
# # 2 = 45
# # 3 = 60
# # 4 = 73
# # 5 = 86
# # 10 = 147
# # 11 = 154 #<- Sseqtest har flowproblemer da Sseqtest_155 = inf da seqtest_155 = inf
# # - Bemærk at problemet med 11 fremkommer idet vi har overflow i tælleren af seqtest_155,
# # således at x**154 * eta**154 =~ 2.13*10^307, mens
# # x**155 =~ 2.605*10^161, eta**155 =~ 8.08335*10^147, således at man skulle tro at Python ville
# # skrive x**155 * eta**155 =~2.106*10^309 -> men i stedet får vi inf.
# # - Dette giver mening idet vi i udregningen opererer i dobbelt precision (altså med 64-bit floating point tal)
# # og at vi med double precisions 11 bit eksponent
# # kan få tal op til 2*2^1023 = 2^1024 =~1.17977*10^308, som vi ved led 155 netop er over.
# #----
# #Bemærk da også at Python informerer os om dette i form af fejlbeskeden;
# # "testprog3.py:35: RuntimeWarning: overflow encountered in multiply
# #   seqtest = (x**n * eta**n / np.math.factorial(n)) * np.exp(- eta * x)"
# #----
# #- Et fiks kan være at bytte om på placeringen af e^{-eta x} og eksempelvis x^n eller eta^n,
# # da det at gange disse to rigtig store tal sammen er det der resulterer i et overflow.
# #!!!!!!!!!!!!!!!!!!
# # - -------- ----- - - - Denne implementation virker delvist; For x = 11 sker det i stedet at summen stopper ved led 159
# # (Sseq_159 er sidste sum) og ikke pga. overflow, men på grund af epsilonkriteriet.
#
# # ------------ PAS DOG PÅ!!!!:
# # e^(-eta*x) bliver også meget småt for store x, og har potentiale til at underflow
# # - Vi vil få underflow her for eta = 9 og fra x = 79 og opefter
# #!!!!!!!!!!!!!!!!!
#
# #Bemærk også at
# # np.math.factorial(155) = 478914290146339387633577523906302272217629
# # 5591337767174070096339929153381622433264146569329274347655956110484
# # 3723115869360207491754290766610032162743824754778064799181105243338
# # 8019613945268755989625594021562850841480674038961663314493440000000
# # 0000000000000000000000000000000 =~ 4.789 * 10^273
# # og at vi har 171! =~ 1.24*10^309, således at vi også i nævner vil have overflow, givet at
# # Python opbevarer np.math.factorial som double precision 64 bit tal.
#
#
#
# #expomat2(A_20, x = qq)
# #print('expm\n', expm(A_20*qq))
#
# #-----------------------------------------
# #09-10-20 14.43 opg 2.5;
# #
# # import numpy as np
# #
# # from numpy.linalg import matrix_power
# # from scipy.linalg import expm
# #
# # def expomat3(A, x, N=10**2, eps=10**(-8)):
# #     #----------------------!!!!!!!!!!!!
# #     # Implementation af matrix expotential ud fra (ligning (3)).
# #     # Input er en kvadratisk matrix A, en skalar x, og evt. ændrede beføjelser af N og eps.
# #     # Programmet stopper efter N trin, eller gennem brug af ligning (4) kriteriet
# #     # - Her er det Sseqtest-variablen skal være > 1 - eps.
# #     # Vi bemærker, at vi har undgået .append-løsninger, og har inkluderet alt det tunge maskineri indenfor én for-loop.
# #     #-----------------------!!!!!!!!!!!
# #
# #
# #     if np.shape(A)[0] != np.shape(A)[1]:  # Simpel "Passer dimensionerne (er A kvadratisk?)"-test
# #         raise AttributeError("A skal være en kvadratisk matrix")
# #
# #     I = np.identity(np.shape(A)[0]).astype(np.int64)
# #     A = A.astype(np.float64)  # Evt. konvertering af A til en matrix med elementer af datatype
# #     # 'float 64 bit'
# #
# #     # Da vi har at a_ii <= - sum_{{j=1}_j \ne i}^n{aij}, og a_{i\ne j}>=0 vil max af (-1)*diagonalelementerne
# #     # være max af (-1)*alle elementer i rækken, hvorfor den inderste np.max-funktion er skrevet som den er.
# #     # - Man kunne dog sagtens forestille sig at det ville være komputationelt billigere at bede Python specifikt om at
# #     # kigge langs diagonalen - Her er altså en videreudviklingsmulighed
# #
# #     #Bemærk også at vi har brug for to max funktionen her, idet np.max(-A, axis = 1) giver en
# #     # vektor med max-værdien for hver række, og det er denne vi skal have max af i definitionen af eta.
# #     m = 2**(np.ceil(np.log(x)/np.log(2))).astype(np.float64) #-Hermed begrænser vi x til x/m til at ligge mellem 0 og 1
# #     x = (x/m).astype(np.float64)
# #
# #     eta = np.max(np.max(-A, axis=1))
# #
# #     P = (I + ((1/eta) * A)).astype(np.float64)
# #     Sseqtest = 0
# #     Sseq = 0
# #
# #     for n in range(0, N + 1):
# #         #Udregning af følgen bag vores teststørrelse.
# #         seqtest = (x**n * eta**n / np.math.factorial(n)) * np.exp(- eta * x)
# #         #Printfunktion til at udforske tælleren af seqtest
# #         print('x**{} = {},\n eta**{} = {},\n x**{}*eta**{} = {}'.format(n,x**n, n, eta**n, n, n, x**n * eta**n))
# #
# #         Sseqtest += seqtest
# #         print('\nseqtest_{} = {}.  Sseqtest_{} = {}'.format(n, seqtest, n, Sseqtest))
# #         if Sseqtest <= 1 - eps:
# #             Sseq += seqtest * (matrix_power(P, n))**m
# #             print('\nSseq_{} =\n{}'.format(n, Sseq))
# #         else:
# #             print('\n1 - eps = {}.\nVi stopper ved trin {} da Sseqtest_{} = {} > 1 - eps.'.format(1 - eps, n - 1, n, Sseqtest))
# #             print('Sseq_{} =\n{}'.format(n - 1, Sseq))  # Vi skal have n-1 her, da n-1 fortsat er mindre end eps fra exp(Ax) i inf-norm
# #             break
# #     return Sseq
# #
# #     # -----
# #
# # A = np.array([[-5, 2, 3],[2, -6, 4],[4, 5, -9]])
# # A_20 = A * 1/20
# #
# #
# # qq = 11
# # expomat3(A, x = qq, N=10**3)
# # print('expm\n', expm(A*qq))
# #
# # #Lav graf over nedenstående
# # # 1 = 29
# # # 2 = 45
# # # 3 = 60
# # # 4 = 73
# # # 5 = 86
# # # 10 = 147
# # # 11 = 154 #<- Sseqtest har flowproblemer da Sseqtest_155 = inf da seqtest_155 = inf
# # # - Bemærk at problemet med 11 fremkommer idet vi har overflow i tælleren af seqtest_155,
# # # således at x**154 * eta**154 =~ 2.13*10^307, mens
# # # x**155 =~ 2.605*10^161, eta**155 =~ 8.08335*10^147, således at man skulle tro at Python ville
# # # skrive x**155 * eta**155 =~2.106*10^309 -> men i stedet får vi inf.
# # # - Dette giver mening idet vi i udregningen opererer i dobbelt precision (altså med 64-bit floating point tal)
# # # og at vi med double precisions 11 bit eksponent
# # # kan få tal op til 2*2^1023 = 2^1024 =~1.17977*10^308, som vi ved led 155 netop er over.
# # #----
# # #Bemærk da også at Python informerer os om dette i form af fejlbeskeden;
# # # "testprog3.py:35: RuntimeWarning: overflow encountered in multiply
# # #   seqtest = (x**n * eta**n / np.math.factorial(n)) * np.exp(- eta * x)"
# # #----
# # #- Et fiks kan være at bytte om på placeringen af e^{-eta x} og eksempelvis x^n eller eta^n,
# # # da det at gange disse to rigtig store tal sammen er det der resulterer i et overflow.
# # #!!!!!!!!!!!!!!!!!!
# # # - -------- ----- - - - Denne implementation virker delvist; For x = 11 sker det i stedet at summen stopper ved led 159
# # # (Sseq_159 er sidste sum) og ikke pga. overflow, men på grund af epsilonkriteriet.
# #
# # # ------------ PAS DOG PÅ!!!!:
# # # e^(-eta*x) bliver også meget småt for store x, og har potentiale til at underflow
# # # - Vi vil få underflow her for eta = 9 og fra x = 79 og opefter
# # #!!!!!!!!!!!!!!!!!
# #
# # #Bemærk også at
# # # np.math.factorial(155) = 478914290146339387633577523906302272217629
# # # 5591337767174070096339929153381622433264146569329274347655956110484
# # # 3723115869360207491754290766610032162743824754778064799181105243338
# # # 8019613945268755989625594021562850841480674038961663314493440000000
# # # 0000000000000000000000000000000 =~ 4.789 * 10^273
# # # og at vi har 171! =~ 1.24*10^309, således at vi også i nævner vil have overflow, givet at
# # # Python opbevarer np.math.factorial som double precision 64 bit tal.
# #
# #
# #
# # #expomat2(A_20, x = qq)
# # #print('expm\n', expm(A_20*qq))
# #
# #
# #-------------------------------
# #09-10-20 16.26 opg 2.5
# # import numpy as np
# #
# # from numpy.linalg import matrix_power
# # from scipy.linalg import expm
# #
# # def expomat3(A, x, N=10**2, eps=10**(-8)):
# #     #----------------------!!!!!!!!!!!!
# #     # Implementation af matrix expotential ud fra (ligning (3)).
# #     # Input er en kvadratisk matrix A, en skalar x, og evt. ændrede beføjelser af N og eps.
# #     # Programmet stopper efter N trin, eller gennem brug af ligning (4) kriteriet
# #     # - Her er det Sseqtest-variablen skal være > 1 - eps.
# #     # Vi bemærker, at vi har undgået .append-løsninger, og har inkluderet alt det tunge maskineri indenfor én for-loop.
# #     #-----------------------!!!!!!!!!!!
# #
# #
# #     if np.shape(A)[0] != np.shape(A)[1]:  # Simpel "Passer dimensionerne (er A kvadratisk?)"-test
# #         raise AttributeError("A skal være en kvadratisk matrix")
# #
# #     I = np.identity(np.shape(A)[0]).astype(np.int64)
# #     A = A.astype(np.float64)  # Evt. konvertering af A til en matrix med elementer af datatype
# #     # 'float 64 bit'
# #
# #     # Da vi har at a_ii <= - sum_{{j=1}_j \ne i}^n{aij}, og a_{i\ne j}>=0 vil max af (-1)*diagonalelementerne
# #     # være max af (-1)*alle elementer i rækken, hvorfor den inderste np.max-funktion er skrevet som den er.
# #     # - Man kunne dog sagtens forestille sig at det ville være komputationelt billigere at bede Python specifikt om at
# #     # kigge langs diagonalen - Her er altså en videreudviklingsmulighed
# #
# #     #Bemærk også at vi har brug for to max funktionen her, idet np.max(-A, axis = 1) giver en
# #     # vektor med max-værdien for hver række, og det er denne vi skal have max af i definitionen af eta.
# #     m = 2**(np.ceil(np.log(x)/np.log(2))).astype(np.float64) #-Hermed begrænser vi x til x/m til at ligge mellem 0 og 1
# #     y = (x/m).astype(np.float64)
# #
# #     eta = np.max(np.max(-A, axis=1))
# #
# #     P = (I + ((1/eta) * A)).astype(np.float64)
# #     Sseqtest = 0
# #     Sseq = 0
# #     #Udregning af følgen bag vores teststørrelse.
# #     seqtest = [(y**n * eta**n / np.math.factorial(n)) * np.exp(- eta * y) for n in range(0,N+1)]
# #     Sseqlist = [seqtest[n] * matrix_power(P,n) for n in range(0, N+1)]
# #     print('type(seqtest) = {}\ntype(Sseqlist) = {}'.format(type(seqtest), type(Sseqlist)))
# #     print('seqtest = \n{}\n\nSseqlist = \n{}'.format(seqtest, Sseqlist))
# #     for n in range(0, N + 1):
# #         Sseqtest = (np.sum(seqtest[0:n+1]))**m
# #         print('Sseqtest = {}'.format(Sseqtest))
# #
# #         Sseq = (np.sum(Sseqlist[0:n+1]))**m
# #         #Printfunktion til at udforske tælleren af seqtest
# #         #print('x**{} = {},\n eta**{} = {},\n x**{}*eta**{} = {}'.format(n,x**n, n, eta**n, n, n, x**n * eta**n))
# #
# #         if Sseqtest <= 1 - eps:
# #             Sseq = (np.sum(Sseqlist[0:n+1]))**m
# #             print('\nSseq_{} =\n{}'.format(n, Sseq))
# #         else:
# #             print('\n1 - eps = {}.\nVi stopper ved trin {} da Sseqtest_{} = {} > 1 - eps.'.format(1 - eps, n - 1, n, Sseqtest))
# #             print('Sseq_{} =\n{}'.format(n - 1, Sseq))  # Vi skal have n-1 her, da n-1 fortsat er mindre end eps fra exp(Ax) i inf-norm
# #             break
# #     return Sseq
# #
# #     # -----
# #
# # A = np.array([[-5, 2, 3],[2, -6, 4],[4, 5, -9]])
# # A_20 = A * 1/20
# #
# #
# # qq = 1
# # expomat3(A, x = qq, N=2)
# # #print('expm\n', expm(A*qq))
# #
# # #Lav graf over nedenstående
# # # 1 = 29
# # # 2 = 45
# # # 3 = 60
# # # 4 = 73
# # # 5 = 86
# # # 10 = 147
# # # 11 = 154 #<- Sseqtest har flowproblemer da Sseqtest_155 = inf da seqtest_155 = inf
# # # - Bemærk at problemet med 11 fremkommer idet vi har overflow i tælleren af seqtest_155,
# # # således at x**154 * eta**154 =~ 2.13*10^307, mens
# # # x**155 =~ 2.605*10^161, eta**155 =~ 8.08335*10^147, således at man skulle tro at Python ville
# # # skrive x**155 * eta**155 =~2.106*10^309 -> men i stedet får vi inf.
# # # - Dette giver mening idet vi i udregningen opererer i dobbelt precision (altså med 64-bit floating point tal)
# # # og at vi med double precisions 11 bit eksponent
# # # kan få tal op til 2*2^1023 = 2^1024 =~1.17977*10^308, som vi ved led 155 netop er over.
# # #----
# # #Bemærk da også at Python informerer os om dette i form af fejlbeskeden;
# # # "testprog3.py:35: RuntimeWarning: overflow encountered in multiply
# # #   seqtest = (x**n * eta**n / np.math.factorial(n)) * np.exp(- eta * x)"
# # #----
# # #- Et fiks kan være at bytte om på placeringen af e^{-eta x} og eksempelvis x^n eller eta^n,
# # # da det at gange disse to rigtig store tal sammen er det der resulterer i et overflow.
# # #!!!!!!!!!!!!!!!!!!
# # # - -------- ----- - - - Denne implementation virker delvist; For x = 11 sker det i stedet at summen stopper ved led 159
# # # (Sseq_159 er sidste sum) og ikke pga. overflow, men på grund af epsilonkriteriet.
# #
# # # ------------ PAS DOG PÅ!!!!:
# # # e^(-eta*x) bliver også meget småt for store x, og har potentiale til at underflow
# # # - Vi vil få underflow her for eta = 9 og fra x = 79 og opefter
# # #!!!!!!!!!!!!!!!!!
# #
# # #Bemærk også at
# # # np.math.factorial(155) = 478914290146339387633577523906302272217629
# # # 5591337767174070096339929153381622433264146569329274347655956110484
# # # 3723115869360207491754290766610032162743824754778064799181105243338
# # # 8019613945268755989625594021562850841480674038961663314493440000000
# # # 0000000000000000000000000000000 =~ 4.789 * 10^273
# # # og at vi har 171! =~ 1.24*10^309, således at vi også i nævner vil have overflow, givet at
# # # Python opbevarer np.math.factorial som double precision 64 bit tal.
# #
# #
# #
# # #expomat2(A_20, x = qq)
# # #print('expm\n', expm(A_20*qq))
# #--------------------------------------------------------------
# #09-10-20, Opgave 2.5 16.48
#
# # import numpy as np
# # import scipy.linalg
# # import time
# #
# # from numpy.linalg import matrix_power
# # from scipy.linalg import expm
# #
# #
# # def expomat2(A, x, N=10**2, eps=10**(-8)):
# #     # Implementation af matrix expotential ud fra (ligning (3)).
# #     # Input er en kvadratisk matrix A, en skalar x, og evt. ændrede beføjelser af N og eps.
# #     # Programmet stopper efter N trin, eller gennem brug af ligning (4) kriteriet
# #     # - Her er det Sseqtest-variablen skal være > 1 - eps.
# #     # Vi bemærker, at vi har undgået .append-løsninger, og har inkluderet alt det tunge maskineri indenfor én for-loop.
# #
# #     if np.shape(A)[0] != np.shape(A)[1]:  # Simpel "Passer dimensionerne (er A kvadratisk?)"-test
# #         raise AttributeError("A skal være en kvadratisk matrix")
# #
# #     I = np.identity(np.shape(A)[0]).astype(np.int64)
# #     A = A.astype(np.float64)  # Evt. konvertering af A til en matrix med elementer af datatype
# #     # 'float 64 bit'
# #
# #     # Da vi har at a_ii <= - sum_{{j=1}_j \ne i}^n{aij}, og a_{i\ne j}>=0 vil max af (-1)*diagonalelementerne
# #     # være max af (-1)*alle elementer i rækken, hvorfor den inderste np.max-funktion er skrevet som den er.
# #     # - Man kunne dog sagtens forestille sig at det ville være komputationelt billigere at bede Python specifikt om at
# #     # kigge langs diagonalen - Her er altså en videreudviklingsmulighed
# #
# #     #Bemærk også at vi har brug for to max funktionen her, idet np.max(-A, axis = 1) giver en
# #     # vektor med max-værdien for hver række, og det er denne vi skal have max af i definitionen af eta.
# #
# #     eta = np.max(np.max(-A, axis=1))
# #
# #     P = (I + ((1/eta) * A)).astype(np.float64)
# #     Sseqtest = 0
# #     Sseq = 0
# #
# #     for n in range(0, N + 1):
# #         seqtest = (x**n * eta**n / np.math.factorial(n)) * np.exp(- eta * x)
# #         Sseqtest += seqtest
# #         print('\nseqtest_{} = {}.  Sseqtest_{} = {}'.format(n, seqtest, n, Sseqtest))
# #         if Sseqtest <= 1 - eps:
# #             Sseq += seqtest * matrix_power(P, n)
# #             print('\nSseq_{} =\n{}'.format(n, Sseq))
# #         else:
# #             print('\n1 - eps = {}.\nVi stopper ved trin {} da Sseqtest_{} = {} > 1 - eps.'.format(1 - eps, n - 1, n, Sseqtest))
# #             print('Sseq_{} =\n{}'.format(n - 1, Sseq))  # Vi skal have n-1 her, da n-1 fortsat er mindre end eps fra exp(Ax) i inf-norm
# #             break
# #     return Sseq
# #
# #
# # def exp3(A,x,eps = 10**(-12)):
# #     t0 = time.time()
# #     N = 0
# #     m = 2**N
# #     x_scale = x/m
# #     while x_scale > 1: # Finder x/m - vi bruger y = np.ceil(log(x)/log(2))
# #         N += 1
# #         m = 2**N
# #         x_scale = x/m
# #     print('scale', x_scale)
# #     result = expomat2(A, x_scale, eps = eps)**m
# #     t1 = time.time()
# #     print('time', t1-t0)
# #     return result
# #
# #
# # A = np.array([[-5, 2, 3],[2, -6, 4],[4, 5, -9]])
# # A_20 = A * 1/20
# #
# # qq = 10
# #
# # exp3(A, x = qq)
# # print('expm\n', expm(A*qq))
# #
# # #
#
# #2.5 20:25
# def expomat3(A, x, M = 2 * 10**2, eps = 10**(-10)):
#
#     if np.shape(A)[0] != np.shape(A)[1]:  # Simpel "Passer dimensionerne (er A kvadratisk?)"-test
#         raise AttributeError("A skal være en kvadratisk matrix")
#
#     #t_st = time.time()
#
#     A = A.astype(np.float64)
#
#     m = np.int64((2**(np.floor(np.log(x)/np.log(2))))) # x vil være i (1,2] <- udregnet på baggrund af at løse ulighederne 2^N\in(1,2)
#
#     y = x/m
#
#     Sseq = matrix_power(expomat2(A = A, x = y, N = M, eps = eps), m)
#     #t_sl = time.time()
#     #print('Tidsforskel = {}'.format(t_sl-t_st))
#     print('Sseq\n', Sseq)
#     return Sseq
#
#
#
#
#
#
#
#
#
#
#
#
