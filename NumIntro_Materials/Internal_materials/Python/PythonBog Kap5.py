# Python bog kap 5;
# Tidligere arbejde som refereres til i kapitlet kan hos os findes i filen "Der skal plottes.py"

import numpy as np
import matplotlib.pyplot as plt

# N = 100
# values = []
# for n in range(1,N):
#     values.append( (n+1)/n**2 )
# plt.plot(values, 'ro')
# plt.show()

# -
# Nedenfor siger nej, da python starter index af values ved 0 og vi spørger efter element [1], som ikke haves.
# N = 100
# x_1 = 2
# values = [x_1]
# for n in range(1,N):
#     values.append(values[n]/2 + 1/values[n])
# plt.plot(values, 'ro')
# plt.show()

# Vi kan fikse ved;
# #1.; Vi betragter i stedet følgen hvor vi har ændret indekseringen så x_0 = 2, x_n = x_(n-1)/2+1/x_(n-1)
# N = 100
# x_0 = 2
# values = [x_0]
# for n in range(0,N):
#     values.append(values[n]/2 + 1/values[n])
# plt.plot(values, 'ro')
# plt.show()


# #2. Eller;
# N = 100
# x_1 = 2
# values = [x_1]
# for n in range(1,N):
#     values.append(values[n-1]/2 + 1/values[n-1])
# plt.plot(values, 'ro')
# plt.show()

# #3.; Eller vi kan fikse problemet med indeksering ved at indse, at programmeringen også kan laves ved;
# N = 100
# x_1 = 2
# values = [x_1]
# for n in range(1,N):
#     values.append(values[-1]/2 + 1/values[-1])
# plt.plot(values, 'ro')
# plt.show()

# -
# #Alternativt vil vi evt kunne lave index transformationer lidt mere eksplicit;
# #Nedenstående er dog meget let eksempel...
# N = 100
# values = [ 2 ]
# for n1base in range(1, N):
#     n0base = n1base - 1
#     values.append(values[n0base]/2 + 1/values[n0base])
# plt.plot(values, 'ro')
# plt.show()

# ------ Kap 5.5
# #-x_n = 1/(n*ln(n)) #Klar konvergens mod 0 idet n*ln(n)->inf, n->inf
# N = 100
# values = []
# for n in range(1,N):
#     values.append(1/(n*np.log(n)))
# plt.plot(values, 'ro')
# #plt.semilogy(values, 'ro')
# plt.show()

# #- x_n = 5/n + e^(-n)
# N = 100
# values = []
# for n in range(1,N):
#     values.append(5/n + np.exp(-n))
# plt.plot(values, 'ro')
# #plt.semilogy(values, 'ro')
# plt.show()

# Også klar konvergens mod 0.


# ------
# Vi laver nice plot;
# # - Se også "Der skal plottes.py"
# N = 100
# values = [2]
# for n in range(1, N):
#     values.append(values[n-1]/2 + 1/values[n-1])
# plt.figure(1)
# plt.plot(values , 'ro')
# plt.title('Convergence Plot')
# plt.xlabel('$n$') #Bemærk at dette laver "Math mode" til aksetitlerne
# plt.ylabel('$x_n$') #Bemærk at dette laver "Math mode" til aksetitlerne
# plt.grid(True)
# plt.show()

# - Vi kan ikke helt se om vi går mod 1.4, noget tæt på 1.4 eller om der bliver spruget rundt frem og tilbage ved 1.4,
# Vi bruger derfor;

# N = 100
# values = [2]
# for n in range(1, N):
#     values.append(values[n-1]/2 + 1/values[n-1])
# plt.figure(1)
# plt.semilogy(values , 'ro')
# plt.title('Convergence Plot')
# plt.xlabel('$n$') #Bemærk at dette laver "Math mode" til aksetitlerne
# plt.ylabel('$x_n$') #Bemærk at dette laver "Math mode" til aksetitlerne
# plt.grid(True)
# plt.show()
#
# #<- Hvad dælan sker der?! - Jeg synes ikke dette gør det nemmere at se noget som helst?
#
# #Vi kan også bruge;
# N = 100
# values = [2]
# for n in range(1, N):
#     values.append(values[n-1]/2 + 1/values[n-1])
# plt.figure(1)
# plt.loglog(values , 'bo') #laver både logx og log y
# plt.title('Convergence Plot')
# plt.xlabel('$n$') #Bemærk at dette laver "Math mode" til aksetitlerne
# plt.ylabel('$x_n$') #Bemærk at dette laver "Math mode" til aksetitlerne
# plt.grid(True)
# plt.show()


# ------------- Fra Onsdag 3 haves;

# print('----')

# N_1 = 100
#
# x_1 = [1]
#
# for i in range(1,N_1+1):
#     x_1.append(.5*x_1[-1])
#
# plt.plot(x_1,"ro")
# plt.show()
#
#
# plt.semilogy(x_1, "ro")
# plt.show()

# Linear convergence towards 0

# -
#
# N_2 = 100
#
# x_2 = [1]
#
# for i in range(1,N_2+1):
#     x_2.append(.5/i*x_2[-1])
#
# #plt.plot(x_2,"ro")
# #plt.show()
#
#
# plt.semilogy(x_2, "ro")
# plt.show()

# Super linear convergence towards 0

# -
# print('----')
#
# N_3 = 10
#
# x_3 = [10]
#
# for i in range(1,N_3+1):
#     x_3.append(.5 * x_3[-1] * 1/(x_3[-1]))
#
# #plt.plot(x_2,"ro")
# #plt.show()
#
#
# plt.semilogy(abs(x_3 - np.sqrt(2)), "ro") #Underflow
# plt.show()

# ------------------ 5.7 Konvergensrater
#

eps_01415 = 0.9
eps_01617 = 0.4
c_14 = 0.5
c_015 = 2
C_1617 = 2

N = 100
val14 = [eps_01415]
val15 = [eps_01415]
val16 = [eps_01617]
val17 = [eps_01617]

for n in range(1, N + 1):
    val14.append(c_14 * val14[n - 1])
    # c_015 *= 0.9
    val15.append(0.9 ** n * c_015 * val15[n - 1])  # c_n = 9/10*c_(n-1) => c_n = (9/10)^2*c_(n-2)
    # => c_n = (9/10)^q*c_(n-q) => c_n = (9/10)^n*c_0
    val16.append(C_1617*val16[n-1]**2)
    val17.append(C_1617*val17[n-1]**3)

# plt.figure(1)
# p14, = plt.plot(val14 , 'r-o', label='Linear', markersize=5, lw=1)
# p15, = plt.plot(val15 , 'g-x',label='Super Linear', markersize=5, lw = 1)
# p16, = plt.plot(val16 , 'b-+',label='Quadratic', markersize=10, lw = 1)
# p17, = plt.plot(val17 , 'm-d',label = 'Cubic', markersize=3, lw = 1)
# plt.legend(handles = [p14, p15 , p16, p17]) # Tilføjer beskrivelsestag(label) - Fjern evt eks. p17 og se forskel
# plt.title('Orders of Convergence Plot')
# plt.xlabel('$n$')
# plt.ylabel('$x_n$')
# plt.grid(True)
# plt.show()
#
# plt.figure(2)
# p14, = plt.semilogy(val14 , 'r-o', label='Linear', markersize=5, lw=1)
# p15, = plt.semilogy(val15 , 'g-x',label='Super Linear', markersize=5, lw = 1)
# p16, = plt.semilogy(val16 , 'b-+',label='Quadratic', markersize=10, lw = 1)
# p17, = plt.semilogy(val17 , 'm-d',label = 'Cubic', markersize=3, lw = 1)
# plt.legend(handles = [p14, p15 , p16, p17]) # Tilføjer beskrivelsestag(label) - Fjern evt eks. p17 og se forskel
# plt.title('Orders of Convergence Log Plot')
# plt.xlabel('$n$')
# plt.ylabel('$\log{(x_n)}$')
# plt.grid(True)
# plt.show()
#
# plt.figure(3)
# p14, = plt.loglog(val14 , 'r-o', label='Linear', markersize=5, lw=1)
# p15, = plt.loglog(val15 , 'g-x',label='Super Linear', markersize=5, lw = 1)
# p16, = plt.loglog(val16 , 'b-+',label='Quadratic', markersize=10, lw = 1)
# p17, = plt.loglog(val17 , 'm-d',label = 'Cubic', markersize=3, lw = 1)
# plt.legend(handles = [p14, p15 , p16, p17]) # Tilføjer beskrivelsestag(label) - Fjern evt eks. p17 og se forskel
# plt.title('Orders of Convergence Log-Log Plot')
# plt.xlabel('$\log{(n)}$')
# plt.ylabel('$\log{(x_n)}$')
# plt.grid(True)
# plt.show()

#??????????????? - Hvordan kaldes et af disse figures? - kan man lave sammensætninger af dem i subplots?
#-> Mit bedste bud er at gemme hver af Figurene og så indsætte dem som billeder;
#!!!!!!!!!!!! SKIDTET VIRKER IKKE!!! :(
# # import matplotlib.image as mpimg
# #
# # img1 = mpimg.imread('Figuresubplottest1.png')
# # img2 = mpimg.imread('Figuresubplottest%s.png' %2) # forsøg
# # img3 = mpimg.imread('Figuresubplottest3.png')
# #
# # plt.imshow(img1)
# #
# # fig = plt.figure()
# # ax = fig.add_subplot(1, 3, 1)
# # imgplot = plt.imshow(img1)
# #
# # ax = fig.add_subplot(1, 3, 2)
# # imgplot = plt.imshow(img2)
# #
# # ax = fig.add_subplot(1, 3, 3)
# # imgplot = plt.imshow(img3)




























































