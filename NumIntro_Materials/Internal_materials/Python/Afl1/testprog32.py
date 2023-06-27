import numpy as np

from numpy.linalg import matrix_power
from scipy.linalg import expm

def expomatn(A, N=10**2, eps=10**(-8)):
    # Implementation af matrix expotential ud fra (ligning (3)).
    # Input er en kvadratisk matrix A, en skalar x, og evt. ændrede beføjelser af N og eps.
    # Programmet stopper efter N trin, eller gennem brug af ligning (4) kriteriet
    # - Her er det Sseqtest-variablen skal være > 1 - eps.
    # Vi bemærker, at vi har undgået .append-løsninger, og har inkluderet alt det tunge maskineri indenfor én for-loop.

    if np.shape(A)[0] != np.shape(A)[1]:  # Simpel "Passer dimensionerne (er A kvadratisk?)"-test
        raise AttributeError("A skal være en kvadratisk matrix")

    I = np.identity(np.shape(A)[0]).astype(np.int64)
    A = A.astype(np.float64)  # Evt. konvertering af A til en matrix med elementer af datatype
    # 'float 64 bit'

    # Da vi har at a_ii <= - sum_{{j=1}_j \ne i}^n{aij}, og a_{i\ne j}>=0 vil max af (-1)*diagonalelementerne
    # være max af (-1)*alle elementer i rækken, hvorfor den inderste np.max-funktion er skrevet som den er.
    # - Man kunne dog sagtens forestille sig at det ville være komputationelt billigere at bede Python specifikt om at
    # kigge langs diagonalen - Her er altså en videreudviklingsmulighed

    #Bemærk også at vi har brug for to max funktionen her, idet np.max(-A, axis = 1) giver en
    # vektor med max-værdien for hver række, og det er denne vi skal have max af i definitionen af eta.

    eta = np.max(np.max(-A, axis=1))

    P = (I + ((1/eta) * A)).astype(np.float64)
    Sseqtest = 0
    Sseq = 0

    for n in range(0, N + 1):
        seqtest = (x**n * np.exp(- eta * x) / np.math.factorial(n)) * eta**n
        print('x**{} = {},\n np.exp(-eta * x) = {},\n x**{}*np.exp(- eta * x) = {}'.format(n,x**n, np.exp(- eta * x), n, x**n * np.exp(- eta * x)))
        print('np.math.factorial({}) = {}'.format(n, np.math.factorial(n)))
        Sseqtest += seqtest
        print('\nseqtest_{} = {}.  Sseqtest_{} = {}'.format(n, seqtest, n, Sseqtest))
        if Sseqtest > 1 - eps:
            print('\n1 - eps = {}.\nVi stopper ved trin {} da Sseqtest_{} = {} > 1 - eps.'.format(1 - eps, n - 1, n, Sseqtest))
            print('Sseq_{} =\n{}'.format(n - 1, Sseq))  # Vi skal have n-1 her, da n-1 fortsat er mindre end eps fra exp(Ax) i inf-norm
            break
    return Sseq

    # -----

A = np.array([[-5, 2, 3],[2, -6, 4],[4, 5, -9]])
A_20 = A * 1/20


qq = 14
expomat2test(A, x = qq, N=10**3)
print('expm\n', expm(A*qq))

#Lav graf over nedenstående
# 1 = 29
# 2 = 45
# 3 = 60
# 4 = 73
# 5 = 86
# 10 = 147
# 11 = 154 #<- Sseqtest har flowproblemer da Sseqtest_155 = inf da seqtest_155 = inf
# - Bemærk at problemet med 11 fremkommer idet vi har overflow i tælleren af seqtest_155,
# således at x**154 * eta**154 =~ 2.13*10^307, mens
# x**155 =~ 2.605*10^161, eta**155 =~ 8.08335*10^147, således at man skulle tro at Python ville
# skrive x**155 * eta**155 =~2.106*10^309 -> men i stedet får vi inf.
# - Dette giver mening idet vi i udregningen opererer i dobbelt precision (altså med 64-bit floating point tal)
# og at vi med double precisions 11 bit eksponent
# kan få tal op til 2*2^1023 = 2^1024 =~1.17977*10^308, som vi ved led 155 netop er over.

#- Et fiks kan være at bytte om på placeringen af e^{-eta x} og eksempelvis x^n eller eta^n,
# da det at gange disse to rigtig store tal sammen er det der resulterer i et overflow.

#Bemærk også at
# np.math.factorial(155) = 478914290146339387633577523906302272217629
# 5591337767174070096339929153381622433264146569329274347655956110484
# 3723115869360207491754290766610032162743824754778064799181105243338
# 8019613945268755989625594021562850841480674038961663314493440000000
# 0000000000000000000000000000000 =~ 4.789 * 10^273
# og at vi har 171! =~ 1.24*10^309, således at vi også i nævner vil have overflow, givet at
# Python opbevarer np.math.factorial som double precision 64 bit tal.



#expomat2test(A_20, x = 1)
#print('expm\n', expm(A_20))





