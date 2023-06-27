# # # # import numpy as np
# # # #
# # # # from numpy.linalg import matrix_power
# # # #
# # # # def infmatnorm(A):
# # # #     #Inf-matrixnormen udregnet af A
# # # #     return np.max((np.abs(A)).sum(axis=1))
# # # #
# # # #
# # # #
# # # # def expomat2(A, x, N = 10**2, eps = 10**(-8)):
# # # #     # Implementation af matrix expotential ud fra (ligning (3)).
# # # #     # Input er en kvadratisk matrix A, en skalar x, og evt. ændrede beføjelser af N og eps.
# # # #     # Programmet stopper efter N trin, eller gennem brug af ligning (4) kriteriet.
# # # #
# # # #     if np.shape(A)[0] != np.shape(A)[1]: #Simpel "Passer dimensionerne (er A kvadratisk?)"-test
# # # #         raise AttributeError("A skal være en kvadratisk matrix")
# # # #
# # # #     I = np.identity(np.shape(A)[0]).astype(np.int64)
# # # #     A = A.astype(np.float64) #Evt. konvertering af A til en matrix med elementer af datatype
# # # #     #'float 64 bit' - Herved kan vi lave betydeligt mere præcise beregninger, og dette
# # # #     #viser sig at være vigtigt i dette tilfælde.
# # # #
# # # #     #Da vi har at a_ii <= - sum_{{j=1}_j \ne i}^n{aij}, og a_{i\ne j}>=0 vil max af (-1)*diagonalelementerne
# # # #     #være max af (-1)*alle elementer i rækken
# # # #     eta = np.max(-A, axis = 1)
# # # #
# # # #     P = (I + 1/eta * A).astype(np.float64)
# # # #     Sseqtest = 0
# # # #     Sseq = 0
# # # #
# # # #     seqP = []
# # # #     for n in range (0, N+1):
# # # #         seqtest = (x**n * eta**n / np.math.factorial(n))
# # # #         #seqP.append(seqtest*matrix_power(P,n))
# # # #         Sseqtest += seqtest
# # # #
# # # #         if Sseqtest > 1 - eps:
# # # #
# # # #             Sseq += seqtest * matrix_power(P,n)
# # # #
# # # #     #-----
# # # #
# # # #     for n in range(0,N+1):
# # # #         print('seq_{} =\n{}'.format(n, seq[n]))
# # # #
# # # #         S += seq[n] #S_n = S_n-1 + seq_n for n>=1
# # # #         print('S_{} =\n{}.'.format(n,S))
# # # #         else:
# # # #             print('eps = {}.\nVi stopper ved trin {} da ||seq_{}||_inf = {} < eps.'.format(eps, n-1, n, seqinfnormtest))
# # # #             print('S_{} =\n{}'.format(n-1,S)) #Vi skal have n-1 her, da n-1 fortsat er mindre eps
# # # #             break
# # # #     return S
# # # #------------------------------------------------------------
# # # #exp2 (virker);
# # # import numpy as np
# # #
# # # from numpy.linalg import matrix_power
# # # from scipy.linalg import expm
# # #
# # # def expomat2(A, x, N=10**2, eps=10**(-8)):
# # #     # Implementation af matrix expotential ud fra (ligning (3)).
# # #     # Input er en kvadratisk matrix A, en skalar x, og evt. ændrede beføjelser af N og eps.
# # #     # Programmet stopper efter N trin, eller gennem brug af ligning (4) kriteriet
# # #     # - Her er det Sseqtest-variablen skal være > 1 - eps.
# # #     # Vi bemærker, at vi har undgået .append-løsninger, og har inkluderet alt det tunge maskineri indenfor én for-loop.
# # #
# # #     if np.shape(A)[0] != np.shape(A)[1]:  # Simpel "Passer dimensionerne (er A kvadratisk?)"-test
# # #         raise AttributeError("A skal være en kvadratisk matrix")
# # #
# # #     I = np.identity(np.shape(A)[0]).astype(np.int64)
# # #     A = A.astype(np.float64)  # Evt. konvertering af A til en matrix med elementer af datatype
# # #     # 'float 64 bit'
# # #
# # #     # Da vi har at a_ii <= - sum_{{j=1}_j \ne i}^n{aij}, og a_{i\ne j}>=0 vil max af (-1)*diagonalelementerne
# # #     # være max af (-1)*alle elementer i rækken, hvorfor den inderste np.max-funktion er skrevet som den er.
# # #     # - Man kunne dog sagtens forestille sig at det ville være komputationelt billigere at bede Python specifikt om at
# # #     # kigge langs diagonalen - Her er altså en videreudviklingsmulighed
# # #
# # #     #Bemærk også at vi har brug for to max funktionen her, idet np.max(-A, axis = 1) giver en
# # #     # vektor med max-værdien for hver række, og det er denne vi skal have max af i definitionen af eta.
# # #
# # #     eta = np.max(np.max(-A, axis=1))
# # #
# # #     P = (I + ((1/eta) * A)).astype(np.float64)
# # #     Sseqtest = 0
# # #     Sseq = 0
# # #
# # #     for n in range(0, N + 1):
# # #         seqtest = (x**n * eta**n / np.math.factorial(n)) * np.exp(- eta * x)
# # #         Sseqtest += seqtest
# # #         print('\nseqtest_{} = {}.  Sseqtest_{} = {}'.format(n, seqtest, n, Sseqtest))
# # #         if Sseqtest <= 1 - eps:
# # #             Sseq += seqtest * matrix_power(P, n)
# # #             print('\nSseq_{} =\n{}'.format(n, Sseq))
# # #         else:
# # #             print('1 - eps = {}.\nVi stopper ved trin {} da Sseqtest_{} = {} > 1 - eps.'.format(1 - eps, n - 1, n, Sseqtest))
# # #             print('Sseq_{} =\n{}'.format(n - 1, Sseq))  # Vi skal have n-1 her, da n-1 fortsat er mindre end eps fra exp(Ax) i inf-norm
# # #             break
# # #     return Sseq
# # #
# # #     # -----
# # #
# # # A = np.array([[-5, 2, 3],[2, -6, 4],[4, 5, -9]])
# # # A_20 = A * 1/20
# # #
# # # expomat2(A, x = 1)
# # # print('expm\n', expm(A))
# # #
# # # #expomat1(A_20, x = 1)
# # # #print(expm(A_20))
# # #
# # #
# # #
# # #
# # #
# # #-------------------------------------------------
# # #exp1 (Virker);
# # import numpy as np
# #
# # #1.
# # from numpy.linalg import matrix_power
# # from scipy.linalg import expm
# #
# # #----
# # # Meta kommentarer;
# # #Vi kunne sagtens lave vores egne enkle "Matrixpower" og "factorial funktioner" - Men da de allerede
# # # eksisterer og sikkert er bedre skrevet end hvad vi kunne, vælger jeg bare at importerer dem.
# # # Vi bemærker også at da vi eksempelvis i Python bog kap 7 har lavet lignende summer til den vi
# # # laver i denne opgave, kunne vi have lavet en module implementation.
# # # - Opgaven beder dog om at regne fra ligning (1) direkte, så vi laver en mere direkte implementation.
# # #----
# #
# # #------------
# # #Personlige tanker;
# # #Hvis np array er hurtigere kan man så lave li9st comprehension med np array og hvordan
# # #Tjek om A er "nxn"
# # # Hvordan får vi gentagende matrix produkt og ikke bare at hæve elementerne til en eller anden orden?
# # # Vi ved at matrix exponential altid konvergerer - så hvorfor ikke bare lade n fortsætte sålænge tilføjelser
# # # er større end epsilon?
# #
# # #Er nuværende god måde at stoppe på? - Hvad nu hvis følgen sank ned under epsilon i kun et trin, og så stak opad?
# #
# #
# # #------------
# #
# # #-------------------
# # # Testcenter;
# #
# # QQ = np.array([[1,2],[3,4]])
# # # # # QQ2 = QQ**2 # - Vi har muligvis et problem
# # # # print(QQ)
# # # # # print(QQ2)
# # # #
# # # # print(np.shape(QQ)[0])
# # #
# # # print('the power of the matrix QQ of 2 is\n', matrix_power(QQ, 2))
# # #
# # # print(np.math.factorial(3))
# #
# #
# # # def expomatT(A, x, N = 10**3, eps = 10**(-8)):
# # #     # Implementation af matrix expotential direkte fra definitionen (ligning (1)).
# # #     # Input er en kvadratisk matrix A, en skalar x, og evt. ændrede beføjelser af N og eps.
# # #     # Programmet stopper efter N trin, eller hvis tilføjelserne til afsnitssummerne
# # #     # er mindre end eps.
# # #
# # #     if np.shape(A)[0] != np.shape(A)[1]: #Simpel "Passer dimensionerne (er A kvadratisk?)"-test
# # #         raise AttributeError("A skal være en kvadratisk matrix")
# # #     S = 0
# # #
# # #     #-----
# # #     # List comprehension på ledene vi senere skal summe;
# # #     # - bemærk at vi også kunne have gjort dette eksempelvis med en for-loop,
# # #     # og at en for-loop i dette tilfælde ville have nogle fordele i forbindelse med
# # #     # stop kriteriet eps i den efterfølgende sum - Dette kunne også løses med en conditional list comprehension,
# # #     # men det burde ikke gøre den helt store forskel.
# # #     #-----
# # #
# # #     seq = [(x**n / (np.math.factorial(n)))*matrix_power(A, n) for n in range(0,N+1)]
# # #     for n in seq:
# # #         if np.abs(seq[n]) >= eps:
# # #             S += seq[n]
# # #             print('S_{} = {}. seq_{} = {}'.format(n,S,n,seq[n]))
# # #         else:
# # #             print('eps = {}.\nVi stopper ved trin {} da |seq_{}| = {} < eps = True.'.format(eps, n-1, n, np.abs(seq[n])))
# # #             print('S_{} = {}'.format(n-1,S))
# # #             break
# # #     return S
# #
# #
# # # T = np.array([[1,-2, 3],[4,5,6], [7,-8, 9]])
# # # print(T)
# # # ER = (np.abs(T)).sum(axis=1)
# # # print(ER)
# # # ERM = np.max(ER)
# # # print(ERM)
# # #
# # # print(T*1/20)
# #
# #
# # #print(T.sum(axis = 0))
# #
# # # expomat1(QQ, 2)
# #
# #
# #
# #
# # #-------------------
# #
# # #----------------------------
# # #Storage
# # # def expomat1old(A, x, N = 10**3, eps = 10**(-8)):
# # #     # Implementation af matrix expotential direkte fra definitionen (ligning (1)).
# # #     # Input er en kvadratisk matrix A, en skalar x, og evt. ændrede beføjelser af N og eps.
# # #     # Programmet stopper efter N trin, eller hvis tilføjelserne til afsnitssummerne (målt i inf-normen)
# # #     # er mindre end eps.
# # #
# # #     if np.shape(A)[0] != np.shape(A)[1]: #Simpel "Passer dimensionerne (er A kvadratisk?)"-test
# # #         raise AttributeError("A skal være en kvadratisk matrix")
# # #     S = 0
# # #
# # #     #-----
# # #     # List comprehension på ledene vi senere skal summe;
# # #     # - bemærk at vi også kunne have gjort dette eksempelvis med en for-loop,
# # #     # og at en for-loop i dette tilfælde ville have nogle fordele i forbindelse med
# # #     # stop kriteriet eps i den efterfølgende sum - Dette kunne også løses med en conditional list comprehension,
# # #     # men det burde ikke gøre den helt store forskel.
# # #
# # #     seq = [(x**n / (np.math.factorial(n)))*matrix_power(A, n) for n in range(0,N+1)]
# # #     #-----
# # #
# # #     for n in range(0,N+1):
# # #         print('seq_{} =\n{}'.format(n, seq[n]))
# # #
# # #         seqinfnormtest = np.max((np.abs(seq[n])).sum(axis=1)) #infnorm af seq[n]
# # #         if seqinfnormtest >= eps:
# # #             S += seq[n] #S_n = S_n-1 + seq_n for n>=1
# # #             print('S_{} =\n{}.'.format(n,S))
# # #         else:
# # #             print('eps = {}.\nVi stopper ved trin {} da ||seq_{}||_inf = {} < eps = True.'.format(eps, n-1, n, seqinfnormtest))
# # #             print('S_{} =\n{}'.format(n-1,S)) #Vi skal have n-1 her, da n-1 fortsat er mindre eps
# # #             break
# # #      return S
# #
# # #--------
# #
# # # def expomat1(A, x, N = 10**2, eps = 10**(-8)):
# # #     # Implementation af matrix expotential direkte fra definitionen (ligning (1)).
# # #     # Input er en kvadratisk matrix A, en skalar x, og evt. ændrede beføjelser af N og eps.
# # #     # Programmet stopper efter N trin, eller hvis tilføjelserne til afsnitssummerne (målt i inf-normen)
# # #     # er mindre end eps.
# # #
# # #     if np.shape(A)[0] != np.shape(A)[1]: #Simpel "Passer dimensionerne (er A kvadratisk?)"-test
# # #         raise AttributeError("A skal være en kvadratisk matrix")
# # #     S = 0
# # #
# # #     #-----
# # #     # List comprehension på ledene vi senere skal summe;
# # #     # - bemærk at vi også kunne have gjort dette eksempelvis med en for-loop,
# # #     # og at en for-loop i dette tilfælde ville have nogle fordele i forbindelse med
# # #     # stop kriteriet eps i den efterfølgende sum - Dette kunne også løses med en conditional list comprehension,
# # #     # men det burde ikke gøre den helt store forskel.
# # #
# # #     seq = [(x**n / (np.math.factorial(n)))*matrix_power(A, n) for n in range(0,N+1)]
# # #     #-----
# # #
# # #     for n in range(0,N+1):
# # #         print('seq_{} =\n{}'.format(n, seq[n]))
# # #
# # #         seqinfnormtest = infmatnorm(seq[n]) #infnorm af seq[n]
# # #         if seqinfnormtest >= eps:
# # #             S += seq[n] #S_n = S_n-1 + seq_n for n>=1
# # #             print('S_{} =\n{}.'.format(n,S))
# # #         else:
# # #             print('eps = {}.\nVi stopper ved trin {} da ||seq_{}||_inf = {} < eps = True.'.format(eps, n-1, n, seqinfnormtest))
# # #             print('S_{} =\n{}'.format(n-1,S)) #Vi skal have n-1 her, da n-1 fortsat er mindre eps
# # #             break
# # #     return S
# #
# # #expomat1(np.identity(5), 1, N = 100) #-Vi ser at vi kommer tæt på en diagonalmatrix fuld af
# # #eulers tal
# #
# #
# # #----------------------------
# #
# #
# #
# # #------------------------------------
# # #Implementering;
# # #
# # def infmatnorm(A):
# #     #Inf-matrixnormen udregnet af A
# #     return np.max((np.abs(A)).sum(axis=1))
# #
# #
# #
# # def expomat1(A, x, N = 10**2, eps = 10**(-8)):
# #     # Implementation af matrix expotential direkte fra definitionen (ligning (1)).
# #     # Input er en kvadratisk matrix A, en skalar x, og evt. ændrede beføjelser af N og eps.
# #     # Programmet stopper efter N trin, eller hvis tilføjelserne til afsnitssummerne (målt i inf-normen)
# #     # er mindre end eps.
# #
# #     if np.shape(A)[0] != np.shape(A)[1]: #Simpel "Passer dimensionerne (er A kvadratisk?)"-test
# #         raise AttributeError("A skal være en kvadratisk matrix")
# #     S = 0
# #
# #     A = A.astype(np.float64) #Evt. konvertering af A til en matrix med elementer af datatype
# #     #'float 64 bit' - Herved kan vi lave betydeligt mere præcise beregninger, og dette
# #     #viser sig at være vigtigt i dette tilfælde.
# #
# #     #-----
# #     # List comprehension på ledene vi senere skal summe;
# #     # - bemærk at vi også kunne have gjort dette eksempelvis med en for-loop,
# #     # og at en for-loop i dette tilfælde ville have nogle fordele i forbindelse med
# #     # stop kriteriet eps i den efterfølgende sum - Dette kunne også løses med en conditional list comprehension,
# #     # men det burde ikke gøre den helt store forskel.
# #
# #     seq = [(x**n / (np.math.factorial(n)))*matrix_power(A, n) for n in range(0,N+1)]
# #     #-----
# #
# #     for n in range(0,N+1):
# #         print('seq_{} =\n{}'.format(n, seq[n]))
# #
# #         seqinfnormtest = infmatnorm(seq[n]) #infnorm af seq[n]
# #         if seqinfnormtest >= eps:
# #             S += seq[n] #S_n = S_n-1 + seq_n for n>=1
# #             print('S_{} =\n{}.'.format(n,S))
# #         else:
# #             print('\neps = {}.\nVi stopper ved trin {} da ||seq_{}||_inf = {} < eps.'.format(eps, n-1, n, seqinfnormtest))
# #             print('S_{} =\n{}'.format(n-1,S)) #Vi skal have n-1 her, da n-1 fortsat er mindre eps
# #             break
# #     return S
# #
# #
# # A = np.array([[-5, 2, 3],[2, -6, 4],[4, 5, -9]])
# # A_20 = A * 1/20
# #
# # expomat1(A, x = 1)
# # print(expm(A))
# #
# # #expomat1(A_20, x = 1)
# # #print(expm(A_20))
# #
# # #Passer indtil sidste decimal
# #
# # #------------------------------------
# # #
# # #
# # import numpy as np
# #
# # from numpy.linalg import matrix_power
# # from scipy.linalg import expm
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
# #         #Udregning af følgen bag vores teststørrelse. Bemærk at formatet hvorved udregningen er skrevet op
# #         # betinger
# #         seqtest = (x**n * eta**n / np.math.factorial(n)) * np.exp(- eta * x)
# #         print('x**{} = {}, eta**{} = {}, x**{}*eta**{} = {}'.format(n,x**n, n, eta**n, n, n, x**n * eta**n))
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
# #     # -----
# #
# # A = np.array([[-5, 2, 3],[2, -6, 4],[4, 5, -9]])
# # A_20 = A * 1/20
# #
# #
# # qq = 11
# # expomat2(A, x = qq, N=10**3)
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
# #--------------------
# # #09-10-20 17.54 2.5 virker ikke
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
# #
#
#
# # fra prog4 dog uden prog4 kl 20:26
# import numpy as np
# import scipy.linalg
# import time
#
# from numpy.linalg import matrix_power
# from scipy.linalg import expm
#
# #Vi bruger tidligere implementering til den nye - se den nye (til opgave 3.3) nedenfor i expomat4
#
# def infmatnorm(A):
#     #Inf-matrixnormen udregnet af A
#     return np.max((np.abs(A)).sum(axis=1))
#
# def expomat1(A, x, N = 10**2, eps = 10**(-8)):
#     # Implementation af matrix expotential direkte fra definitionen (ligning (1)).
#     # Input er en kvadratisk matrix A, en skalar x, og evt. ændrede beføjelser af N og eps.
#     # Programmet stopper efter N trin, eller hvis tilføjelserne til afsnitssummerne (målt i inf-normen)
#     # er mindre end eps.
#
#     if np.shape(A)[0] != np.shape(A)[1]: #Simpel "Passer dimensionerne (er A kvadratisk?)"-test
#         raise AttributeError("A skal være en kvadratisk matrix")
#     S = 0
#
#     A = A.astype(np.float64) #Evt. konvertering af A til en matrix med elementer af datatype
#     #'float 64 bit' - Herved kan vi lave betydeligt mere præcise beregninger, og dette
#     #viser sig at være vigtigt i dette tilfælde, idet vi ellers hurtigt opnår flowproblemer.
#
#     #-----
#     # List comprehension på ledene vi senere skal summe;
#     # - bemærk at vi også kunne have gjort dette eksempelvis med en for-loop,
#     # og at en for-loop i dette tilfælde ville have nogle fordele i forbindelse med
#     # stop kriteriet eps i den efterfølgende sum - Dette kunne også løses med en conditional list comprehension,
#     # men det burde ikke gøre den helt store forskel.
#
#     seq = [(x**n / (np.math.factorial(n)))*matrix_power(A, n) for n in range(0,N+1)]
#     #-----
#
#     for n in range(0,N+1):
#         #print('seq_{} =\n{}'.format(n, seq[n]))
#
#         seqinfnormtest = infmatnorm(seq[n]) #infnorm af seq[n]
#         if seqinfnormtest >= eps:
#             S += seq[n] #S_n = S_n-1 + seq_n for n>=1
#             #print('S_{} =\n{}.'.format(n,S))
#         else:
#             #print('\neps = {}.\nVi stopper ved trin {} da ||seq_{}||_inf = {} < eps.'.format(eps, n-1, n, seqinfnormtest))
#             #print('S_{} =\n{}'.format(n-1,S)) #Vi skal have n-1 her, da n-1 fortsat er mindre eps
#             break
#     return S
#
#
# def expomat2(A, x, N = 2 * 10**2, eps=10**(-8)):
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
#         seqtest = (x**n * eta**n / np.math.factorial(n)) * np.exp(- eta * x)
#         Sseqtest += seqtest
#         #print('\nseqtest_{} = {}.  Sseqtest_{} = {}'.format(n, seqtest, n, Sseqtest))
#         if Sseqtest <= 1 - eps:
#             Sseq += seqtest * matrix_power(P, n)
#             #print('\nSseq_{} =\n{}'.format(n, Sseq))
#         else:
#             #print('\n1 - eps = {}.\nVi stopper ved trin {} da Sseqtest_{} = {} > 1 - eps.'.format(1 - eps, n - 1, n, Sseqtest))
#             #print('Sseq_{} =\n{}'.format(n - 1, Sseq))  # Vi skal have n-1 her, da n-1 fortsat er mindre end eps fra exp(Ax) i inf-norm
#             break
#     return Sseq
#
#
#
#
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
#     #print('Sseq\n', Sseq)
#     return Sseq
#
#
# #def expomat4():
#
#
#
#
#
# def matexpmforskel(A, x, w = 3, M = 200, eps = 10**(-8)):
#     if np.shape(A)[0] != np.shape(A)[1]:  # Simpel "Passer dimensionerne (er A kvadratisk?)"-test
#         raise AttributeError("A skal være en kvadratisk matrix")
#     A = A.astype(np.float64)
#
#     if w == 1:
#         print(infmatnorm(expomat1(A,x,M,eps) - expm(A*x)))
#         return infmatnorm(expomat1(A,x,M,eps) - expm(A*x))
#
#     if w == 2:
#         print(infmatnorm(expomat2(A,x,M,eps) - expm(A*x)))
#         return infmatnorm(expomat2(A,x,M,eps) - expm(A*x))
#
#     if w == 3:
#         print(infmatnorm(expomat3(A,x,M,eps) - expm(A*x)))
#         return infmatnorm(expomat3(A,x,M,eps) - expm(A*x))
#
#
#
#
# qq = 1
#
# A = np.array([[-5, 2, 3],[2, -6, 4],[4, 5, -9]])
# A_20 = A * 1/20
#
#
# QWE = matexpmforskel(A,x = qq, w = 3)
# print('QWE', QWE)
#
# #expomat3(A, x = qq)
# #print('expm\n', expm(A*qq))
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
