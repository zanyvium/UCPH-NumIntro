
#-----
#19.36 prog1
import numpy as np

#1.
from numpy.linalg import matrix_power
from scipy.linalg import expm

#------------------------------------
#Implementering;
#
def infmatnorm(A):
    #Inf-matrixnormen udregnet af A
    return np.max((np.abs(A)).sum(axis=1))



def expomat1(A, x, N = 2 * 10**2, eps = 10**(-8)):
    # Implementation af matrix expotential direkte fra definitionen (ligning (1)).
    # Input er en kvadratisk matrix A, en skalar x, og evt. ændrede beføjelser af N og eps.
    # Programmet stopper efter N trin, eller hvis tilføjelserne til afsnitssummerne (målt i inf-normen)
    # er mindre end eps.

    if np.shape(A)[0] != np.shape(A)[1]: #Simpel "Passer dimensionerne (er A kvadratisk?)"-test
        raise AttributeError("A skal være en kvadratisk matrix")
    S = 0

    A = A.astype(np.float64) #Evt. konvertering af A til en matrix med elementer af datatype
    #'float 64 bit' - Herved kan vi lave betydeligt mere præcise beregninger, og dette
    #viser sig at være vigtigt i dette tilfælde, idet vi ellers hurtigt opnår flowproblemer.

    #-----
    # List comprehension på ledene vi senere skal summe;
    # - bemærk at vi også kunne have gjort dette eksempelvis med en for-loop,
    # og at en for-loop i dette tilfælde ville have nogle fordele i forbindelse med
    # stop kriteriet eps i den efterfølgende sum - Dette kunne også løses med en conditional list comprehension,
    # men det burde ikke gøre den helt store forskel.

    seq = [(x**n / (np.math.factorial(n)))*matrix_power(A, n) for n in range(0,N+1)]
    #-----

    for n in range(0,N+1):
        print('seq_{} =\n{}'.format(n, seq[n]))

        seqinfnormtest = infmatnorm(seq[n]) #infnorm af seq[n]
        if seqinfnormtest >= eps:
            S += seq[n] #S_n = S_n-1 + seq_n for n>=1
            print('S_{} =\n{}.'.format(n,S))
        else:
            print('\neps = {}.\nVi stopper ved trin {} da ||seq_{}||_inf = {} < eps.'.format(eps, n-1, n, seqinfnormtest))
            print('S_{} =\n{}'.format(n-1,S)) #Vi skal have n-1 her, da n-1 fortsat er mindre eps
            break
    return S


A = np.array([[-5, 2, 3],[2, -6, 4],[4, 5, -9]])
A_20 = A * 1/20

qq = 1
#expomat1(A, x = qq, N=10**3)
#print('expm\n', expm(A*qq))

expomat1(A_20, x = qq)
print('expm\n', expm(A_20*qq))

#Passer indtil sidste decimal

#------------------------------------










#-----
#19.35 prog2;
import numpy as np

from numpy.linalg import matrix_power
from scipy.linalg import expm

def expomat2(A, x, N = 2 * 10**2, eps = 10**(-8)):
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
        seqtest = (x**n * eta**n / np.math.factorial(n)) * np.exp(- eta * x)
        Sseqtest += seqtest
        print('\nseqtest_{} = {}.  Sseqtest_{} = {}'.format(n, seqtest, n, Sseqtest))
        if Sseqtest <= 1 - eps:
            Sseq += seqtest * matrix_power(P, n)
            print('\nSseq_{} =\n{}'.format(n, Sseq))
        else:
            print('\n1 - eps = {}.\nVi stopper ved trin {} da Sseqtest_{} = {} > 1 - eps.'.format(1 - eps, n - 1, n, Sseqtest))
            print('Sseq_{} =\n{}'.format(n - 1, Sseq))  # Vi skal have n-1 her, da n-1 fortsat er mindre end eps fra exp(Ax) i inf-norm
            break
    return Sseq

    # -----

A = np.array([[-5, 2, 3],[2, -6, 4],[4, 5, -9]])
A_20 = A * 1/20

qq = 1
expomat2(A, x = qq, N = 3*10**2)
print('expm\n', expm(A*qq))

#expomat2(A_20, x = 1)
#print('expm\n', expm(A_20))

#------------
#19.37 prog3
import numpy as np
import scipy.linalg
import time

from numpy.linalg import matrix_power
from scipy.linalg import expm

#Vi bruger tidligere implementering til den nye - se den nye (til opgave 2.5) nedenfor i expomat3

def expomat2(A, x, N = 2 * 10**2, eps = 10**(-8)):
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
        seqtest = (x**n * eta**n / np.math.factorial(n)) * np.exp(- eta * x)
        Sseqtest += seqtest
        print('\nseqtest_{} = {}.  Sseqtest_{} = {}'.format(n, seqtest, n, Sseqtest))
        if Sseqtest <= 1 - eps:
            Sseq += seqtest * matrix_power(P, n)
            print('\nSseq_{} =\n{}'.format(n, Sseq))
        else:
            print('\n1 - eps = {}.\nVi stopper ved trin {} da Sseqtest_{} = {} > 1 - eps.'.format(1 - eps, n - 1, n, Sseqtest))
            print('Sseq_{} =\n{}'.format(n - 1, Sseq))  # Vi skal have n-1 her, da n-1 fortsat er mindre end eps fra exp(Ax) i inf-norm
            break
    return Sseq




def expomat3(A, x, M = 2 * 10**2, eps = 10**(-10)):


    if np.shape(A)[0] != np.shape(A)[1]:  # Simpel "Passer dimensionerne (er A kvadratisk?)"-test
        raise AttributeError("A skal være en kvadratisk matrix")

    #t_st = time.time()

    A = A.astype(np.float64)

    m = (2**(np.floor(np.log(x)/np.log(2)))) # x vil være i (1,2] <- udregnet på baggrund af at løse ulighederne 2^N\in(1,2)
    y = x/m

    Sseq = ((expomat2(A = A, x = y, N = M, eps = eps))**m)
    print('Sseqwow', Sseq)

    #t_sl = time.time()
    #print('Tidsforskel = {}'.format(t_sl-t_st))
    return Sseq


qq = 10

A = np.array([[-5, 2, 3],[2, -6, 4],[4, 5, -9]])
A_20 = A * 1/20

SWER = expomat3(A, x = qq, M = 200)
print('SWER', SWER)
#QWERT = expomat3(A, x = qq) - expm(A*qq)
#print(QWERT)


#print('expm\n', expm(A*qq))

def matexpmforskel(A, x, w = 3, M = 200, eps = 10**(-8)):
    if np.shape(A)[0] != np.shape(A)[1]:  # Simpel "Passer dimensionerne (er A kvadratisk?)"-test
        raise AttributeError("A skal være en kvadratisk matrix")
    A = A.astype(np.float64)

    if w == 1:
        print(infmatnorm(expomat1(A,x,M,eps) - expm(A*x)))
        return infmatnorm(expomat1(A,x,M,eps) - expm(A*x))

    if w == 2:
        print(infmatnorm(expomat2(A,x,M,eps) - expm(A*x)))
        return infmatnorm(expomat2(A,x,M,eps) - expm(A*x))

    if w == 3:
        print(infmatnorm(expomat3(A,x,M,eps) - expm(A*x)))
        return infmatnorm(expomat3(A,x,M,eps) - expm(A*x))









