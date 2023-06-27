import numpy as np
import time
#import scipy.linalg

from numpy.linalg import matrix_power
from scipy.linalg import expm

#Vi bruger tidligere implementering til den nye - se den nye (til opgave 3.3) nedenfor i expomat4

def infmatnorm(A):
    #Inf-matrixnormen udregnet af A
    return np.max((np.abs(A)).sum(axis=1))

def expomat1(A, x, N = 10**2, eps = 10**(-8)):
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
        #print('seq_{} =\n{}'.format(n, seq[n]))

        seqinfnormtest = infmatnorm(seq[n]) #infnorm af seq[n]
        if seqinfnormtest >= eps:
            S += seq[n] #S_n = S_n-1 + seq_n for n>=1
            #print('S_{} =\n{}.'.format(n,S))
        else:
            #print('\neps = {}.\nVi stopper ved trin {} da ||seq_{}||_inf = {} < eps.'.format(eps, n-1, n, seqinfnormtest))
            #print('S_{} =\n{}'.format(n-1,S)) #Vi skal have n-1 her, da n-1 fortsat er mindre eps
            break
    return S


def expomat2(A, x, N = 2 * 10**2, eps=10**(-8)):
    # Implementation af matrix expotential ud fra (ligning (3)).
    # Input er en kvadratisk matrix A, en skalar x, og evt. ændrede beføjelser af N og eps.
    # Programmet stopper efter N trin, eller gennem brug af ligning (4) kriteriet
    # - Her er det Sseqtest-variablen skal være > 1 - eps.
    # Vi bemærker, at vi har undgået .append-løsninger, og har inkluderet alt det tunge maskineri indenfor én for-loop.

    if np.shape(A)[0] != np.shape(A)[1]:  # Simpel "Passer dimensionerne (er A kvadratisk?)"-test
        raise AttributeError("A skal være en kvadratisk matrix")

    I = np.identity(np.shape(A)[0]).astype(np.int64)
    A = A.astype(np.float64)  # Evt. konvertering af A til en matrix med elementer af datatype

    eta = np.max(np.max(-A, axis=1))

    P = (I + ((1/eta) * A)).astype(np.float64)
    Sseqtest = 0
    Sseq = 0

    for n in range(0, N + 1):
        seqtest = (x**n * eta**n / np.math.factorial(n)) * np.exp(- eta * x)
        Sseqtest += seqtest
        #print('\nseqtest_{} = {}.  Sseqtest_{} = {}'.format(n, seqtest, n, Sseqtest))
        if Sseqtest <= 1 - eps:
            Sseq += seqtest * matrix_power(P, n)
            #print('\nSseq_{} =\n{}'.format(n, Sseq))
        else:
            #print('\n1 - eps = {}.\nVi stopper ved trin {} da Sseqtest_{} = {} > 1 - eps.'.format(1 - eps, n - 1, n, Sseqtest))
            #print('Sseq_{} =\n{}'.format(n - 1, Sseq))  # Vi skal have n-1 her, da n-1 fortsat er mindre end eps fra exp(Ax) i inf-norm
            break
    return Sseq




def expomat3(A, x, M = 2 * 10**2, eps = 10**(-10)):

    if np.shape(A)[0] != np.shape(A)[1]:  # Simpel "Passer dimensionerne (er A kvadratisk?)"-test
        raise AttributeError("A skal være en kvadratisk matrix")

    #t_st = time.time()

    A = A.astype(np.float64)

    m = np.int64((2**(np.floor(np.log(x)/np.log(2))))) # x vil være i (1,2] <- udregnet på baggrund af at løse ulighederne 2^N\in(1,2)

    y = x/m

    Sseq = matrix_power(expomat2(A = A, x = y, N = M, eps = eps), m)
    #t_sl = time.time()
    #print('Tidsforskel = {}'.format(t_sl-t_st))
    #print('Sseq\n', Sseq)
    return Sseq


def expomat4(A,x):
    #tst = time.time()
    if np.shape(A)[0] != np.shape(A)[1]:  # Simpel "Passer dimensionerne (er A kvadratisk?)"-test
        raise AttributeError("A skal være en kvadratisk matrix")
    A = A.astype(np.float64)
    vals, V = np.linalg.eig(A) #Designerer eigenværdier, og eigenvektorer på baggrund af

    # #Hvis A er diagonaliserbar hvis vi har en basis af eigenvektorer for \F^{len(A)}
    # if len(V) != len(A):
    #     raise AttributeError("A er ikke diagonaliserbar")

    D = np.diag(vals) #Implementerer definitionen af D

    Dxexp = np.zeros(np.shape(A)) #Initialisering

    #Vi bruger her opgave 3.1, og indsætter eigenværdierne af A langs diagonalen
    for n in range(0, len(Dxexp)):
        Dxexp[n,n] = np.exp(D[n,n]*x)

    Vinv = np.linalg.inv(V) #Inverse til V

    Axexp = V.dot(Dxexp).dot(Vinv) #Bruger opgave 3.2
    #tsl = time.time()
    #forskel = tsl - tst
    #print('Tidsforskel',forskel)
    #print('Axexp = \n{}'.format(Axexp))

    return Axexp


qq = 1
A = np.array([[-5, 2, 3],[2, -6, 4],[4, 5, -9]])
QQQ = expomat4(A,x=qq)
print(QQQ)



def matexpmforskel(A, x, w = 3, M = 200, eps = 10**(-8)):
    if np.shape(A)[0] != np.shape(A)[1]:  # Simpel "Passer dimensionerne (er A kvadratisk?)"-test
        raise AttributeError("A skal være en kvadratisk matrix")
    A = A.astype(np.float64)

    if w == 1:
        print('||expomat1-expm|| =', infmatnorm(expomat1(A,x,M,eps) - expm(A*x)))
        return infmatnorm(expomat1(A,x,M,eps) - expm(A*x))
    elif w == 2:
        print('||expomat2-expm|| =', infmatnorm(expomat2(A,x,M,eps) - expm(A*x)))
        return infmatnorm(expomat2(A,x,M,eps) - expm(A*x))
    elif w == 3:
        print('||expomat3-expm|| =', infmatnorm(expomat3(A,x,M,eps) - expm(A*x)))
        return infmatnorm(expomat3(A,x,M,eps) - expm(A*x))
    elif w == 4:
        print('||expomat4-expm|| =', infmatnorm(expomat4(A,x) - expm(A*x)))
        return infmatnorm(expomat4(A,x) - expm(A*x))
    elif w == 5:
        print('||expomat4-expomat3|| =', infmatnorm(expomat4(A,x) - expomat3(A,x,M,eps)))
    elif w == 34:
        print('||expomat3-expm||_(x = {}) = {}'.format(x, infmatnorm(expomat3(A,x,M,eps) - expm(A*x))))
        print('||expomat4-expm||_(x = {}) = {}'.format(x, infmatnorm(expomat4(A,x) - expm(A*x))))
    else:
        print('||expomat1-expm|| =', infmatnorm(expomat1(A,x,M,eps) - expm(A*x)))
        print('||expomat2-expm|| =', infmatnorm(expomat2(A,x,M,eps) - expm(A*x)))
        print('||expomat3-expm|| =', infmatnorm(expomat3(A,x,M,eps) - expm(A*x)))
        print('||expomat4-expm|| =', infmatnorm(expomat4(A,x) - expm(A*x)))
        return None


qq = 100
A = np.array([[-5, 2, 3],[2, -6, 4],[4, 5, -9]])
matexpmforskel(A, x = qq, w = 5)




















