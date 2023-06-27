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
        #print('\nseqtest_{} = {}.  Sseqtest_{} = {}'.format(n, seqtest, n, Sseqtest))
        if Sseqtest <= 1 - eps:
            Sseq += seqtest * matrix_power(P, n)
            #print('\nSseq_{} =\n{}'.format(n, Sseq))
        else:
            print('\n1 - eps = {}.\nVi stopper ved trin {} da Sseqtest_{} = {} > 1 - eps.'.format(1 - eps, n - 1, n, Sseqtest))
            #print('Sseq_{} =\n{}'.format(n - 1, Sseq))  # Vi skal have n-1 her, da n-1 fortsat er mindre end eps fra exp(Ax) i inf-norm
            break
    return Sseq




def expomat3(A, x, M = 2 * 10**2, eps = 10**(-10)):
    # I expomat3 udregner vi igen expotentialmatricen af Ax.
    # Vi gør her brug af både "uniformisation og "scaling and squaring".


    if np.shape(A)[0] != np.shape(A)[1]:  # Simpel "Passer dimensionerne (er A kvadratisk?)"-test
        raise AttributeError("A skal være en kvadratisk matrix")

    #t_st = time.time()

    A = A.astype(np.float64)

    m = np.int64((2**(np.floor(np.log(x)/np.log(2))))) # x vil være i (1,2] <- udregnet på baggrund af at løse ulighederne 2^N\in(1,2)

    y = x/m #Vores scalering af x


    # m'te potens af funktionskald til expomat2, som regner expotentialmatricen på baggrund af opgave 2.2 og 2.3.
    # Vi specificerer at vi ønsker at expomat2 tager y som dens x - (vi er efterhånden særligt opmærksomme på scope)
    Sseq = matrix_power(expomat2(A = A, x = y, N = M, eps = eps), m)

    #t_sl = time.time()
    #print('Tidsforskel =', t_sl - t_st)
    #print('Sseq\n', Sseq)
    return Sseq


qq = 100

A = np.array([[-5, 2, 3],[2, -6, 4],[4, 5, -9]])

qwe = expomat3(A, x = qq, M = 200)
print(qwe)
#print('expm\n', expm(A*qq))
