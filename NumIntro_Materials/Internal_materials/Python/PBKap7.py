import numpy as np


# -
# Vi summer 10 første led af 1/n:

# N = 10
# S = 0
# for n in range(1,N+1):
#     S = S + 1/n
# print('The total sum is =', S)
#
# # Vi kan også summe fra en liste;
# #- Enten ved at bede Python om at lægge det næste led til for hvert led i listen;
#
# x = [1., 0.5, 0.33, 0.25, 0.2]
# S = 0
# for x_n in x:
#     S = S + x_n
# print('The total sum is =', S)
#
# #...- eller ved at lave indekseret summering, idet vi får Python til at hente længden af
# # vores liste, og da summer elementer lige så længde vi ikke har summet flere led end
# #listen er lang;
#
# x = [ 1., 0.5, 0.33, 0.25, 0.2]
# N = len(x)
# S = 0
# for n in range(0,N):
#     S = S + x[n]
# print('The total sum is =', S)

# -
# - Vi kan også lave lignende med produkter;
# r = [-2., 2., 0.]
# N = len(r)
# x = 1/2
# P = 0
# for n in range(0,N):
#     P = P * (x-r[n])
# print('The total product is =', P)

# <- AAAAAAAAAAAAAAAAAAAAARH, den virker sku ikke Kaj!!, vi får jo rigtig pænt ganget med 0.

# r = [-2., 2., 0.]
# N = len(r)
# x = 1/2
# P = 1 # Bedre
# for n in range(0,N):
#     P = P * (x-r[n])
# print('The total product is =', P)

# #- Piecewise function - ækvivalent til max funktionen
# x = 2
# y = -3
# f = None
# if x >= y:
#     f = x
# else:
#     f = y
#
# print('f(', x, ',', y, ') = ', f)


# -

# #-> S = sum_(n=1)^(N)(max(x_n, 0)) :
# x = [ 1., 0.5, 0.33, -0.25, 0.2]
# N = len(x)
# S = 0
# for n in range(0,N):
#     if x[n] > 0:
#         S = S + x[n]
# print('The sum of max-terms is =', S)


# -
# Fibonnachi - Vi har vist lavet noget lignende tidligere.
# del x

# x = []
# N = 10
# for n in range(0,N+1):
#     if n <= 1:
#         x.append(1)
#     else:
#         x.append(x[-1] + x[-2])
# print('The sequence is =', x)

# -
# Der findes måder at lave eksempelvis følger meget mere kompakt.
# Gode kodeord at huske i denne sag er "map-funktionen", "lambda-expressions",
# "The filter function", "The zip function", "List comprehensions".

# Hvor vi eksempelvis skulle lave en for-loop for at kigge på følger som 1/n for n = 1,...,10
# kan dette gøres let med eksempelvis map-funktionen;


# values = list(map(lambda n: 1/n, range(1,11)))
# print('vals1', values)
#
# #<- Bemærk at man også kan lave map funktionen gennem funktionskald;
# def detdaelmesmart(n):
#     return 1 / n
#
#
# values2 = list(map(detdaelmesmart, range(1,11)))
# print('vals2', values2)
#
# # Alternativt kan man gøre det endnu kortere ved brug af "list comprehensions";
#
# values3 = [1/n for n in range(1,11)]
# print('vals3', values3)

# ----
# 7.5;
# 1; S_n := sum_{i=0}^{n}{\lrp{\frac{1}{2}}^{n+1}}
# Hvordan gøres dette med sum-funktionen?


# def sevfivoneshort(N=10):
#     # Se NI bog kap 3 vedr. brug af eps-kritérier
#     seq = [(1 / 2) ** (n + 1) for n in range(0, N + 1)]
#     q = np.sum(seq)
#     return q
#
#
# print(sevfivoneshort(N=5))
#
# #-
# print('')
#
# def sevfivonemed(N=10, eps=10**(-8), konvtest=False):
#     # Se NI bog kap 3 vedr. brug af eps-kritérier
#     seq = [(1 / 2) ** (n + 1) for n in range(0, N + 1)]
#     S = 0
#     for i in range(0, N + 1):
#         S += seq[i]
#         print("S_%s =" %i, S)
#         if konvtest == True and np.abs((1 / 2) ** (i + 1)) < eps:
#             print("Forskel mellem sidste to led mindre end eps = %s" %eps, "ved trin %s\n" %i, "S er %s" %S)
#             break
#     return S
#
# sevfivonemed(N = 50, konvtest = True)

# def sevfivonelong(N = 10):
#     #Se NI bog kap 3 vedr. brug af eps-kritérier
#     seq = []
#     for n in range(0,N+1):
#         seq.append((1/2)**(n+1))
#
#     seq = [(1/2)**(n+1) for n in range(0,N+1)]
#     q = np.sum(seq)
#     return q

# - Hvor hurtigt sker dette????!!!!!!!!!!!!!!!!!
#<- !!!!!!!!!!!!!!!!!!!!!!!!!!!-----!!!!!!!!!!!!!!!!!!!!!!!!
#<- Hvordan evaluerer vi hvor hurtigt ting divergerer??!??!?!?!?!


#7.5.2;
# # Hvad går nedenstående lige ud på?
# # - Noget n vælg k? - Altså binomialkoef? - Det lader til at gå op
# # <- men hvorfor?
# def sevfivtwo(n,k):
#     r = 1
#     for i in range(1,k+1):
#         r = r * (n + 1 - i)/i
#         print("r_%s =" %i, r)
#     return r
#
# sevfivtwo(5, 3)


#7.5.3
#
# def sevfivthree(R):
#     a = np.array([[],[]])
#     a[0,0] = 1 # Pas på med indeksering
#     for r in range(2,R+1): #Pas igen på med indeks - vi ændrer forloopets indhold så det passer
#         # fordi python er lort
#         for c in range(1,r+1):
#             if c > 1 and c < r: #equiv 1 < c < r
#                 a[r-1, c-1] = a[r-2, c-2] + a[r-2, c-1]
#             else:
#                 a[r-1, c-1] = 1
#             return a[r-1,:] #<-Der er noget galt her
#
# sevfivthree(3)
#
# #Det virker ikke - <- fejler allerede på a[0,0] = 1 <- find lige ud af hvordan man gør sådan noget.

