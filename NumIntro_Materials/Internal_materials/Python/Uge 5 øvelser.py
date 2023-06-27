import numpy as np
from numpy.linalg import matrix_power #Til Von Neumann
#
# n = 3
# A = np.array([[60,30,20],[30,20,15],[20,15,12]])
# U = np.zeros(np.shape(A))
# L = U.copy
#
# for k in range(0,n):
#     L[k,k] = 1.0 #Bemærk denne form - Vi har med Doolitte at gøre
#     if k == 0: #Specialtilfældet for den første række
#         for j in range(k, n):
#             U[k][j] = A[k][j]
#     else:
#         for j in range(k, n):
#             sum = 0.0
#             for s in range(0,k):
#                 sum += L[k][s]*U[s][j]
#             U[k][j] = A[k][j] - sum
#     if k == 0:
#         for i in range(k,n):
#             L[i][k] = A[i][k]/U[k][k]
#     else:
#         for q in range(k+1,n):
#             sum = 0.0
#             for s in range(0,k):
#                 sum += L[q][s]*U[s][k]
#             L[q][k] =(A[k][q] - sum)/U[k][k]
# print(U)
# print(L)
#
#
# #---------------- -> Til funktion;
#
#
# def doo(A):
#     U = np.zeros(np.shape(A))
#     L = np.zeros(np.shape(A))
#     n = len(A)
#     for k in range(0,n):
#         L[k,k] = 1.0 #Bemærk denne form - Vi har med Doolitte at gøre
#         if k == 0: #Specialtilfældet for den første række
#             for j in range(k, n):
#                 U[k][j] = A[k][j]
#         else:
#             for j in range(k, n):
#                 sum = 0.0
#                 for s in range(0,k):
#                     sum += L[k][s]*U[s][j]
#                 U[k][j] = A[k][j] - sum
#         if k == 0:
#             for i in range(k,n):
#                 L[i][k] = A[i][k]/U[k][k]
#         else:
#             for q in range(k+1,n):
#                 sum = 0.0
#                 for s in range(0,k):
#                     sum += L[q][s]*U[s][k]
#                 L[q][k] =(A[k][q] - sum)/U[k][k]
#         return L,U
#
def doo(A): #Fra Nick
    n = A.shape[0]

    U = np.zeros((n, n), dtype=np.double)
    L = np.eye(n, dtype=np.double)

    for i in range(0, n):
        for j in range(i,n):
            sum = 0
            for k in range(i):
                sum = sum + L[i,k]*U[k,j]
            U[i,j] = A[i,j] - sum
        for j in range(i, n):
            if i == j:
                L[i,i] = 1
            else:
                sum = 0
                for k in range(i):
                    sum = sum + L[j,k]*U[k,i]
                L[j,i] = (A[j,i]-sum)/U[i,i]
    return L, U



# #For motivation af fremadrettet og baggudrettet substitution, se Slide 2 af LU.
# #Der er tale om fremadrettet idet vi har Ax=B for A nedre triangulær og x ukendt, og
# #baggudrettet er Ax=b hvor A er øvre triangulær

def forward(A,b):
    #Kræver en nedre triangulær matrix (hvor diagonal elementerne ikke er 0)
    A = np.float64(A)
    lb = len(A)
    x = np.zeros(lb, dtype=np.double)
    for i in range(0, lb):
        sum = 0
        for j in range(0, lb):
            sum += A[i, j] * x[j]
            #print("i = {}, j = {}, sum = {}".format(i,j,sum))
        x[i] = (b[i] - sum)/A[i, i]
    return x

#Hvordan ville rowswap virke? - vi får sku da aldrig det vi vil have!!! ? - se 5.1?!!!?
# def subsrowswap(A): #Kan vi bruge np.rstack på en smart måde?
#     A_2 = np.zeros(A.shape, dtype=np.double) #Forskel mellem np.double og np.float64?
#     la = len(A)
#     for i in range(0, la):
#         A_2[i] = A[la - i - 1]
#     return A_2

def backward(A,b):
    #Kræver en øvre triangulær matrix (hvor diagonal elementerne ikke er 0)
    A = np.float64(A)
    lb = len(A)
    x = np.zeros(lb, dtype=np.double)
    for i in range(lb-1, -1, -1):
        sum = 0
        for j in range(i, lb):
            sum += A[i, j] * x[j]
            #print("i = {}, j = {}, sum = {}".format(i,j,sum))
        x[i] = (b[i] - sum)/A[i, i]
    return x


# A = np.zeros((7,7))
# A[:,0] = range(1,8)


# U=np.array([[2,1,5],[0,4,7],[0,0,5]])
# print(U)
# b = np.array([7,5,4])

#print(forward(A,b))
#print(backward(A,b))

#print(subsrowswap(A))

#Invers af L;
def l_inverse(L):
    #Tager en invertibel nedre triangulær matrix og inverterer den.
    L = np.float64(L)
    n = L.shape[0]
    b = np.eye(n)
    Linv = np.zeros(L.shape)
    for i in range(n):
        Linv[i] = forward(L,b[i,:]) # kan man gøre dette med rstack? - <- Det er åbenbart ligemeget med b[i,:] eller b[:,i]
    Linv = np.transpose(Linv) # Hvorfor giver overstående den transponerede inverse matrix?
    return Linv

# L = np.array([[2,0,0],[0,4,0],[3,7,5]])
# print(L)
# print(l_inverse(L))
# print(L.dot(l_inverse(L)))


def u_inverse(U):
    #Tager en invertibel nedre triangulær matrix og inverterer den.
    U = np.float64(U)
    n = U.shape[0]
    b = np.eye(n)
    Uinv = np.zeros(U.shape)
    for i in range(n):
        Uinv[i] = backward(U,b[i,:]) # kan man gøre dette med rstack? -
        # <- Det er åbenbart ligemeget med b[i,:] eller b[:,i]
    Uinv = np.transpose(Uinv) # Hvorfor giver overstående den transponerede inverse matrix?
    return Uinv

# U = np.array([[2,0,5],[0,4,7],[0,0,5]])
# print(U)
# print(u_inverse(U))
# print(U.dot(u_inverse(U)))



#Invers af enhver matrix LU-dekomposionérbar matrix A
# gennem brug af Doolittle-LU (fra Nick);
def lu_inverseN(A):
    A = np.float64(A)
    n = A.shape[0]
    b = np.eye(n) #identitetsmatrix som "nxn" - "n" i python format.
    Ainv = np.zeros(A.shape)
    L, U = doo(A)
    for i in range(n):
        y = forward(L, b[i, :]) #Ved at løse Ax=e_i for i in range(0,n)
        # opnås kollonerne af invers matricen til A
        Ainv[i, :] = backward(U, y)
    return Ainv

#Invers af enhver matrix LU-dekomposionérbar matrix A
# gennem brug af L invers og U invers og Doolittle (selvlavet);

def lu_inverseS(A):
    A = np.float64(A)
    L,U = doo(A)
    Ainv = u_inverse(U).dot(l_inverse(L))
    return Ainv
# A = np.array([[2,1,5],[-4,4,7],[6,-10,5]])
# print(A)
# print(lu_inverseS(A))
# print(lu_inverseS(A).dot(A))


####Von Neumann selvlavet;
def VonNeumann(A, N = 100, eps = 10**(-8)):
    # Virker
    A = np.float64(A)
    I = np.eye(len(A))
    B = I - A
    if np.linalg.norm(B) >= 1: #Frob-norm (euclidian-based)
        raise AttributeError("||I-A||>=1")
    S = np.zeros(A.shape, dtype = np.float64)
    dif = 0
    Q = False
    for n in range(0,N+1):
        prevS = S.copy()
        S += matrix_power(B,n)
        dif = np.linalg.norm(prevS - S)
        if dif < eps:
            Q = True
            print("Stoppet ved trin {} med ||S_1-S|| = {}".format(n,dif))
            break
    if Q == False: #Findes en bedre måde ikke at printe to gange på?
        print("Stoppet ved trin {} med ||S_1-S|| = {}".format(n,dif))
    return S

A = np.array([[0.6,0.2,0.1],[0.1,0.5,0.3],[0.5,0.1,0.9]])
#print(A)
#print(VonNeumann(A, eps = 10**(-10))) #Den virker


####Von Neumann fra "algoritme1" slide 5 i kanoniske forelæsning
def Neumann(A, N = 50, eps = 10**(-8)):
    A = np.float64(A)
    I = np.eye(len(A))
    B = I - A
    if np.linalg.norm(B) >= 1: #Frob-norm (euclidian-based)
        raise AttributeError("||I-A||>=1")
    P = B
    S = I
    prevS = np.zeros(np.shape(S))
    n = 0
    while np.linalg.norm(prevS - S) >= eps or n < N:
        prevS = np.copy(S)
        S += P
        P = P.dot(B) #Pas på med at bruge * på matricer!!!
        n += 1
        #print("n = {}, S =\n{}.".format(n,S))
        #print("\nprevS = \n{}".format(prevS))
        #print("diff: {}".format(np.linalg.norm(prevS - S)))
        print(n)
    return S

# A = np.array([[0.6,0.2,0.1],[0.1,0.5,0.3],[0.5,0.1,0.9]])
# print(A)
# print(Neumann(A))



#--------------
#U5O4, P4.2.30;
#Vi stjæler Nicks Crout implementering;
def Crout(A):
    n = A.shape[0]

    L = np.zeros((n,n))
    U = np.zeros((n,n))

    for k in range(n):
        U[k, k] = 1

        for j in range(k, n):
            sum0 = sum([L[j, s] * U[s, k] for s in range(0, j)]) #range from index 0
            L[j, k] = A[j, k] - sum0 #reversed index

        for j in range(k+1, n):
            sum1 = sum([L[k, s] * U[s, j] for s in range(0, j)]) #range from index 0
            U[k, j] = (A[k, j] - sum1) / L[k, k]

    return L, U

# A = np.array([[3,0,1],[0,-1,3],[1,3,0]])
# print(A)
# print("L = \n{}".format(Crout(A)[0]))
# print("\nU = \n{}".format(Crout(A)[1]))
#print(1/A)



### Vi kunne også lave vores egen Crout implementering ved at bruge
# LU-slides side 6 tippet med at gange U's diagonal på den;

def diagonalextract(A,t = False):
    A = np.float64(A)
    diagv = np.diag(A)
    diagA = np.diag(diagv)
    if t == True:
        return diagv
    else:
        return diagA

def CroutfraDoo(A):
    A = np.float64(A)
    L,U = doo(A) #Doolittle faktoriseringen klaret.

    udiagv = np.diag(U) #Vektor med diagonalelementerne af U
    print("udiagv = {}".format(udiagv))
    udiag = np.diag(udiagv) #Diagonalmatrice med U's diagonal
    print("\nudiag = \n{}".format(udiag))

    ###
    #udiag = diagonalextract(U)
    ###

    udiagI = np.diag(np.reciprocal(udiagv)) #Invers matrice til diagonalmatrice med U's diagonal. - Pas på ikke at tage resiprok af
    #hele udiag-matricen, da 1/0 -> inf i Python for ikke-diagonal elementerne. <- Vi tager dermed resiprok af udiagv,
    # og indsætter det så i en matrix.
    print("\nudiagI = \n{}".format(udiagI))

    L = L.dot(udiag) # Definér ny L
    U = udiagI.dot(U) #Definér ny U
    return L,U


# A = np.array([[3,0,1],[0,-1,3],[1,3,0]])
# #print(A)
#
# print("L = \n{}".format(CroutfraDoo(A)[0]))
# print("\nU = \n{}".format(CroutfraDoo(A)[1]))

def CholeskyfraDoo(A):
    #Tjek om A er symmetrisk og positivt definit!!!!
    #Minder meget om CroutfraDoo-funktionen.

    A = np.float64(A)
    L,U = doo(A)
    ocudiagv = diagonalextract(U, True)
    print("ocudiagv = {}".format(ocudiagv))
    #Vi tager sqrt(-1) -> og python ved ikke hvad den skal gøre med komplekse tal åbenbart.
    finL = L.dot(np.diag(np.sqrt(ocudiagv)))
    print("finL\n", finL)
    finuLT = np.diag(np.sqrt(ocudiagv)*np.reciprocal(ocudiagv)).dot(U)
    return finL, finuLT

A = np.array([[3,0,1],[0,-1,3],[1,3,0]])
#print(A)


#print("L = \n{}".format(CholeskyfraDoo(A)[0]))
#print("\nU = \n{}".format(CholeskyfraDoo(A)[1]))

#CholeskyfraDoo(A)



#--------------------------------

print("L = \n{}".format(doo(A)[0]))
print("\nU = \n{}".format(doo(A)[1]))




