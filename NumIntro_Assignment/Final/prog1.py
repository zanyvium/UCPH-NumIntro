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
expomat1(A, x = qq, N=10**3)
print('expm\n', expm(A*qq))

#expomat1(A_20, x = qq)
#print('expm\n', expm(A_20*qq))

#Passer indtil sidste decimal

#------------------------------------


