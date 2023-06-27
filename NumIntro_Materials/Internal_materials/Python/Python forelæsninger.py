from idlelib.idle_test.test_browser import fname
from turtle import shape

import numpy as np
import matplotlib.pyplot as plt

#----
# print("Dingo")
#
#
# name = input('Enter your name: ')
#
#
# print('Hello ' + name + '!\n Welcome to this class!')
#
# name_2 = name.lower()
#
# name_3 = name + name
#
# print('Is name decimal?', name.isdecimal())
#
# print('Is name lower?', name.islower())
#
# #print('Is name printable?', name.printable())
#
#
# #
# a = input('Enter a number: ')
#
# b = 2*a
#
# print(b)


#Vi ser at hvis vi skriver et tal ind, så gentager b bare tallet til os to gange
# i stedet for at gange det med to. - Dette er fordi 'tallet a' registreres som en tekst-streng
# Se derfor følgende løsning;

# a = float(input('Enter a number: '))
#
# b = 2*a
#
# print(b)
#

# -------------------------



# x = []
#
# i = 1
#
# A = True
# while A:
#     z = (1+1/i)**(i)
#     x.append(z)
#     if abs(z-2.71)<.01:
#         A = False
#         print('A "The Rock" Johnson is now false,\n as an alternative to using break')
#         print("The final index is ", i)
#     i += 1


#----------- Mandag2
#Det viser sig at være komputationelt nemmere at regne med numpy arrays end med lists, de fungerer dog meget ens;


# a = np.array([1,2,3])
# a_1 = np.array([1,2,3.1])
# a_2 = np.array([1,2,23], dtype='float32')
# a_3 = np.array([1,2,23], dtype='float64')
# a_4 = np.array([1,2,23], dtype='int32')
# a_5 = np.array([1,2,23], dtype='int64')
# a_6 = np.array([1,2,23.3], dtype='int64')
#
#
#
# print('a data type: ', a.dtype) #da vi opskriver som heltal registreres de også således
# print('a_1 data type: ', a_1.dtype) # Hvis vi skriver bare én af tallene i np-arrayen som decimaltal,
#                                     # bliver datatypen af dataen nu float (i dette tilfælde i 64 bit format)
# print('a_5 data type: ', a_5.dtype) #Vi specificerer datatypen til python
# print('a_6: ', a_6, 'og a_6 data type: ', a_6.dtype) #Vi ser dermed at der er sket en
#                                                       # nedrunding af 23.3 for at få denne til at passe med int-formatet
#
# b = np.array([4,5,6])
#
# c_1 = a + b
# c_2 = a - b
# c_3 = a * b
# c_4 = a / b
#
# print('c1: ', c_1, 'c2: ', c_2, 'c3: ', c_3, 'c4: ', c_4)
#
# print('number of bytes in a: ', a.nbytes) # Hver af de tre tal i arrayen er 32-bit = 4 byte x 3 tal = 12 bytes i alt
# print('number of bytes in a_3: ', a_3.nbytes) # Hver af de tre tal i arrayen er 64-bit = 8 byte x 3 tal = 24 bytes i alt
#
# d = np.array([[1.1,2,3], [4,5,6], [7,8,9]],dtype = 'int32')
# print('d: ', d) #Vi bemærker igen at specificeringen af datatypen afrunder 1.1 til 1 efter floorfunktionen.
#                 #Samtidigt bemærkes at vi har skabt en "to dimensionel array"
#                 # - som er isomorft koncepåt med det at tale om en matrix
# e = np.array([[10,11,12], [13,14,15], [16,17,18]], dtype = 'int32')
#
# f_1 = d + e
# f_2 = d - e
# f_3 = d * e
# f_4 = d / e
# print('')
#
# print('f1:\n', f_1, '\n\n f2:\n', f_2, '\n\nf3:\n ', f_3, '\n\nf4:\n', f_4)
#
# #-
#
# print('')
#
# A = np.zeros((6,2)) #Bemærk dobbelt parentes, vi får 6 rækker, og to søjler - alt sammen fyldt med 0'er
# A_p = np.zeros(shape = (6,3)) # seks rækker tre søjler fyldt med 0'er
# print('A:\n', A)
# print('\nA_p:\n', A_p)
#
# B = np.ones((2,6)) #to rækker seks søjler fyldt med 1'er
# print('\nB:\n', B)
#
# C = np.ones(4) #Rækkevektor med fire elementer, alle sammen 1'er
# print('\nC:\n', C)
#
# D = B * 4
# print('\nD:\n', D)
#
# #-
# print('')
#
# q = np.random.rand() #Genererer pseudo-tilfældige tal baseret på en ligefordeling mellem 0 og 1
# print('q: ', q)
#
# q_0 = q + 1 # Vi translaterer q med +1 så vi får tilfældige tal mellem 1 og 2 # es bedre?
# print('\nq0: ', q_0)
#
# q_1 = 700 * q # Vi skalerer q så vi nu får tilfældige tal mellem 0 og 700 # <- kan dette gøres bedre?
# print('\nq1: ', q_1)
#
# q_2 = np.random.rand(3,2) # Laver en 3 x 2 matrix med ligefordelt udtrukkede pseudo-tilfældige tal i enhedsintervallet
# print('\nq2:\n', q_2)
#
# q_3 = np.random.randn(4,3) #Laver en 4 x 3 matrix med pseudo-tilfældige tal baseret på en standard normalfordeling
# print('\nq3:\n', q_3)
#
# sigma = 5 #bare et eksempelvis valg
# mu = 2 #bare et eksempelvis valg
# q_4 = mu + np.sqrt(sigma) * q_3 #q_4 tager nu tilfældige værdier fra en N(mu, sigma^2)-fordeling
#                                 # for hver indgang i en 4 x 3 matrix
# print('\nq4:\n', q_4)
#
# #<- Hvordan laver vi eksempelvis histogrammer over disse?
#
# q_5 = np.random.randint(1,11, size = (4,3)) #Vi skaber en 4 x 3 matrix med ligefordelt udtrukkede heltal mellem 1 og 11-1
# print('\nq5:\n', q_5)
#
# q_6 = q_5[1,2]
# print('\n[1,2] i q5:\n', q_6) #(anden række og tredje søjle elementet (python tæller fra 0 som en klaphest)
#
# q_7 = q_5[1,0:3]
# print('\nq5[1,0:3]\n', q_7) #Vi betragter anden række (pyhon tæller fra 0 som en klaphest), og tæller elementerne
#                                      # [0,1,2], da Python har slutindeks eksklusiv (som en klaphest)
#
#
# #-
#
# w = np.identity(6) # 6 x 6 identitetsmatrix
# print('\nw:\n', w)
#

#----------Onsdag2

# theta = np.pi/2
#
# b = np.array([np.cos(theta), np.sin(theta)])
# print('b: ', b)
#
# b_1 = np.array([np.exp(1), np.exp(2), np.exp(np.log(10)), np.log(10)])
# print('b_1 :', b_1) #hvorfor i alverden er der sådanne store mellemrum idet vi printer ting?
#
# #-
# print("")
#
# x = np.linspace(-1,1,10) # 10 numbers with equal distance from each other, between -1 and 1 with both endpoints included
# print("x: ", x, "\nlength of x: ", len(x))
#
# x_1 = np.linspace(0,1,10) # 10 numbers with equal distance from each other, between 0 and 1
# print("\nx_1: ", x_1, "\nlength of x_1: ", len(x_1))
#
# x_2 = np.linspace(0,1,11) # 11 numbers with equal distance from each other, between 0 and 1
# print("\nx_2: ", x_2, "\nlength of x_2: ", len(x_2))
#
# x_3 = np.linspace(0,1,10, endpoint = False) # 10 numbers with equal distance from each other, between 0 and 1
# print("\nx_3: ", x_3, "\nlength of x_3: ", len(x_3))
#
# #x_4 = np.linspace(0,1,10, startpoint = False) # 10 numbers with equal distance from each other, between 0 and 1 <- Nope!
# #print("\nx_4: ", x_4, "\nlength of x_4: ", len(x_4)) # <- Denne bliver suuuuuuur!!
#
# x_5 = np.linspace(-np.pi, np.pi, 1000)
# y_5 = np.sin(x_5)
#
# plt.plot(x_5, y_5)
# plt.grid()
# plt.show()
#
# x_6 = np.linspace(-1+.01, 1-.01, 1000)
# y_6 = np.arcsin(x_6)
#
# plt.plot(x_6, y_6)
# plt.grid()
# plt.show()
#
# #-
# # I stedet for at specificerer at man gerne vil have q tal mellem start of slut
# # kan man for heltal sige at man gerne vil have tal mellem start og slut-1, og
# # og at disse skal komme med en trinstørrelse på t.
# # <- vi bruger til dette funktionen 'arange' (ikke arrange)


# start = 3
# slut = 11
# t = 1
#
# u = np.arange(start, slut, t)
# u_1 = np.arange(start,slut) #Som standard er t = 1 sat
# u_2 = np.arange(start,slut, 3)
#
#
# print('u:', u, "\nu_1:", u_1, "\nu_2:", u_2)
#
# #-
# print('')
#
# p = np.arange(3, 31, 2)
# r = 2
# print("p shape: ", p.shape)
# c = int(p.size / r)
# p.shape = (r, int(c)) #tvinger p i størrelse (r, c)
#
# print("p:\n", p)
#
# #-
# #Python er åbenbart endnu mere down in the dumps og kan godt lide at lave følgende lort;
# s = np.array([[1,2],[3,4]])
# o = s
# print('\nOriginal o;\n', o)
#
# s[0,0] = 100
#
# print("\nÆndret s:\n", s)
# print("\nEr o anderledes?\n", o)
#
# #Hvilket er fucked... - !!! FIND UD AF HVORNÅR DETTE SKER!!!
# #Et fiks kan være følgende;
# s_1 = np.array([[1,2],[3,4]])
# o_1 = s_1.copy()
# print('\nOriginal o_1;\n', o_1)
#
# s_1[0,0] = 100
#
# print("\nÆndret s_1:\n", s_1)
# print("\nEr o_1 anderledes?\n", o_1)
#
# s_2 = 5
# o_2 = s_2
#
# print('start o = ', o_2) # b_2 = 5
#
# s_2 = 3
#
# print ('Slut b = ', o_2) # b_2 = 5
#
# #-
#
# k = np.array([[1,2],[3,4]])
# h = np.array([-1,1,1,-1])
#
# #Vi kan ikke lave eksempelvis k+h #<- kan vi lave "prikprodukt"?
# #Hvis vi skal "lægge k og h sammen" må vi ændre formen af én af dem.
# print('h shape ', h.shape)
# print('k shape ', k.shape)
#
# j = k.reshape(h.shape) + h
# #Vi kunne selvfølgelig også lave k.reshape(1,4) eller have lavet reshape på h
# print("j: ", j)
#
# #-
# print('')
# v = np.random.randint(1,11,10) #Fra 1 til 11-1 og vælg træk 10 gange.
# print('v:', v)
# v_s1 = np.sum(v)
# v_s2 = v.sum()
# print("v_s1:", v_s1) #Metode 1 til at lave sum
# print("v_s2:", v_s2) #Metode 2 til at lave sum
#
# v_p1 = np.prod(v)
# v_p2 = v.prod()
# print("v_p1:", v_p1) #Metode 1 til at lave produkt
# print("v_p2:", v_p2) #Metode 2 til at lave produkt
#
# v_mx1 = np.max(v)
# v_mx2 = v.max()
# print("v_mx1:", v_mx1) #Metode 1 til at tage max
# print("v_mx2:", v_mx2) #Metode 2 til at tage max
#
# v_mn1 = np.min(v)
# v_mn2 = v.min()
# print("v_mn1:", v_mn1) #Metode 1 til at tage min
# print("v_mn2:", v_mn2) #Metode 2 til at tage min
#
# v_me1 = np.mean(v)
# v_me2 = v.mean()
# print("v_me1:", v_me1) #Metode 1 til at tage gennemsnit
# print("v_me2:", v_me2) #Metode 2 til at tage gennemsnit
#
# v_std1 = np.std(v)
# v_std2 = v.std()
# print("v_std1:", v_std1) #Metode 1 til at tage standard afvigelse
# print("v_std2:", v_std2) #Metode 2 til at tage standard afvigelse
#
# v_var1 = np.var(v)
# v_var2 = v.var()
# print("v_var1:", v_var1) #Metode 1 til at tage standard afvigelse
# print("v_var2:", v_var2) #Metode 2 til at tage standard afvigelse
#
#
# v_ptp1 = np.ptp(v) #"Point to Point"
# v_ptp2 = v.ptp()
# print("v_ptp1:", v_ptp1) #Metode 1 til at tage differens mellem max og min
# print("v_ptp2:", v_ptp2) #Metode 2 til at tage differens mellem max og min
#
# #-
# print('')
# #Lad os nu kigge på andre brugsmuligheder for diverse funktioner i det vi bruger dem på dele af objekter;
# #Vi kan eksempelvis, idet vi betragter en matrix, tage maximum af hver række eller hver søjle:
#
# g = np.array([[1,2], [3,4]])
# print("\ng:\n", g)
#
# g_maxs = g.max(axis = 0) # axis = 0 giver søjle åbenbart
# print("\nmaxafhver søjle:\n", g_maxs) #Vi får en vektor som indeholder max elementet i hver søjle
# #(Max i første søjle af g er 3, max af anden søjle er 4)
#
#
# g_maxr = np.max(g, axis = 1) # axis = 1 giver rækker åbenbart
# print("\nmaxafhver række:\n", g_maxr) #Vi får en vektor som indeholder max elementet af hver række
# #(Max i første række af g er 2, max af anden række er 4)
#
# #Lignende med sum, min, gennemsnit osv...
#
# #Vi forestiller os at vi også ville kunne gøre dette ved at indekserer over søjlerne eller rækkerne...
#
# #-
# print('')
# z = np.array([[1,2], [3,4]])
# print('z:\n', z)
#
# n = z.transpose()
# print('\nn:\n', n)
#
# #Vi kan også til tider ønske at betragte en matrix som en vektor;
#
# n_1 = z.flatten()
# print('\nn_1:\n', n_1)
#
# #Bemærk også at python ikke ændrer shit med flatten;
# z[0,0] = 100
# print('\nn_1 er ny?:\n', n_1, "- Nej")
#
# #Men 'ravel' - som gør det samme som flatten, lader sig ændre;
# z[0,0] = 1
# n_2 = z.ravel()
# print('\nn_2:\n', n_2)
#
# z[0,0] = 100
# print('\nn_2 er ny?:\n', n_2, "- ja!")
#
# #-
# print('')
#
# #Vi betragter matrix-vektor-operationer
# l = np.array([[1,2], [3,4]])
# m = np.ones(l.shape) #Matrix med 1'er i form af l
#
# f = l + m
# print("l + m:\n", f) #elementvis addition
#
# f_1 = l * m
# print("\nl * m:\n", f_1, "Ikke matrix mult, men elementvis mult") #Ikke matrix mult, men elementvis mult
#
# f_2 = np.matmul(l,m) #Vil også bruges til at regne prikprodukt af to vektorer
# print("\nMatrix mult af l & m:\n", f_2, "Matrix mult, ikke elementvis mult") #Matrix mult
#
# f_3 = np.linalg.det(l)
# print("\nDet(l): ", f_3)
#
# #-
# print('')
#
# e = np.array([0, 1, 0, 1])
# i = np.array([-1, 2, 2, 1])
#
# ei_1 = np.vstack([e, i, e-i, e+i]) #Sammensætter de forskellige input ved at give hver sin egen række
# ei_2 = np.hstack([e, i, e-i, e+i]) #Sammensætter ved konkatination
#
# print('ei_1:\n', ei_1)
# print('\nei_2:', ei_2)

# ---------- Mandag 3
# print('')
#
# a = np.arange(-5,6)
#
# print('a:', a)
#
# print('a[1:5]:', a[1:5])
#
# print('a[1:6:2]:', a[1:6:2])
#
# print('a[:3]:', a[:3]) #Start from beginning and go to element [3 - 1]
#
# print('a[2:]:', a[2:]) #Start from element [2] and go to end
#
# print('a[::2]:', a[::2]) # Every second element of a
#
# a[::2] = 100 # Set every second element of a to 100 <- Bemærk at vi starter fra det første element i a
#             # ergo har vi 1.,3.,5.,7.,... = 100 og ikke 2.,4.,6.,8.,...
# print('a, 1., 3., ...:', a)
#
# #Hvis vi vil have 2.,4.,6.,... kan vi;
# a = np.arange(-5,6) #reset for at illustrerer at vi laver 2.,4.,6.,... = 100
#
# a[1::2] = 100
#
# print ('a, 2., 4., ...:', a)
#
#
#
# #-
# print('')
#
# b = np.arange(18).reshape(3,6)
#
# print('b:\n', b, '\n')
#
# print('b[0,:]:\n', b[0,:]) #hele første række
#
# print('\nb[:,1]:\n', b[:,1]) #hele anden søjle
#
# print('\nb[0:2,:]:\n', b[0:2,:]) #hele første og anden række
#
# print('\nb[0:2,3]:\n', b[0:2,3]) #Vi kan også hente elementer således
#
# #print('\nb[::2]:\n', b[::2])
#
# print('\nb[:,::2]:\n', b[:,::2]) #Alle rækker, hvert andet element
#
# print('\nb[0:2,::2]:\n', b[0:2, ::2]) #Første to rækker, hvert andet element
#
# print('\nb[0:2,::2]:\n', b[0:2, ::2]) #Første to rækker, hvert andet element
#
# #Hvordan første to søjler, hvert andet element?
#
# print('\nb:\n', b, '\n')
#
# print('\nb[:,::-1]:\n', b[:, ::-1]) #Printer elementerne i hver række i omvendt rækkefølge
#
# print('\nb[::-1,::-1]:\n', b[::-1, ::-1]) #mærkelig dobbelt omvendt
#
# #-
# print('')
#
# b[0,:] = -b[0,:]
# print('new b:\n', b)
#
# #-
# print('')
#
# id1 = [1, 6, 0]
#
# c = np.arange(-5,5)
#
# c_1 = c[id1]
#
# print('\nc:', c)
# print('\nc_1:', c_1)
#
# c_2 = c[c>0]
#
# print('\nc_2:', c_2)
#
# c_3 = c[(c>-2) & (c<=3)]
#
# print('\nc_3:', c_3)
#
# d = c>-2
#
# print('\nd:', d)
#
# d_1 = ((c>-2) & (c<=3)) #a.any() or a.all() ???
#
# print('\nd_1:', d_1)
#
# #Hvordan gøres dette? - > print(c[d_1] == c_3)
#
# #-
# print('')
#
# e = np.arange(1,19).reshape(3,6)
# print('e:\n', e)
#
# id2 = [[0,1,2], [0,1,2]]
# print('\nid2:\n', id2)
#
# id2_1  = tuple(id2) #Immutable???
#
# print('\nid2_1:\n', id2_1)
#
# e_1 = e[id2_1] #elementerne [e[0,0], e[1,1], e[2,2]] betragtes, og samles i en array
#
# print('\ne_1:\n', e_1)
#
# id3 = tuple([[0,1,2], [1,3,5]])
#
# e_2 = e[id3] # Betragt elementerne [e[0,1], e[1,3], e[2,5]]
# print('\ne:\n', e)
#
# print('\ne_2:\n',  e_2)
#
# #-
# print('')
# f = np.arange(1,19).reshape(3,6)
#
# print('f:\n', f)
# print('\nf.sum():', f.sum())
#
# f_1 = f[:,0] #1. søjle af f
#
# print('\nf_1.sum():', f_1.sum())
#
# f_2 = f.sum(axis = 0) #Summen af hver søjle lavet til en vektor
#
# print('\nf_2:\n', f_2)
#
# f_3 = f.sum(axis = 1) # Summen af hver række lavet til en vektor
#
# print('\nf_3:\n', f_3)
#
# f_4 = f.max() #Max af hele f
#
# print('\nf_4:\n', f_4)
#
# f_5 = f.max(axis = 0) #Max af hver søjle
#
# print('\nf_5:\n', f_5)
#
# f_6 = f.max(axis = 1) #Max af hver række
#
# print('\nf_6:\n', f_6)
#
# #-
# f = np.arange(1,19).reshape(3,6)
# print('')
#
# #Bemærk at imens np.sum(f) = f.sum(), vil sum(f) = f_2
#
#
# #-
# print('')
#
# g = np.random.randint(1,21, size = (4,3)) #trækker tilfældige heltal mellem 0 og 20 og laver dem til en 4x3 matrix
#
# print('g:\n', g)
#
# g_1 = g.argmax() #Giver lokation på højeste element i .flatten af g
#                 # --- Bemærk at der ved flere max værdier kun bliver indkodet én af dem.
#                 # ??? Hvordan fås lokation i matrix-form? - Se unravel.index nedenfor.
#
# print('\ng_1:\n', g_1)
#
# g_2 = g.flatten()[g_1] #Det højeste element er altså
#
# print('\ng_2:\n', g_2)
#
# g_3 = g.argmin()
#
# print('\ng_3:\n', g_3)
#
# g_4 = np.unravel_index(indices = g.argmax(), shape = g.shape) #Finder også kun én af max
#
# print('\ng_4:\n', g_4)
#
# g_5 = g[g_4]
#
# print('\ng_5:\n',g_5)
#
# #-
# print('')
#
# h = np.random.rand(1,100)
# print('h:\n', h)
#
# h_1 = h.mean(axis = 0)
#
# print('\nh_1:\n',h_1)
#
# h_2 = h.mean(axis = 1)
#
# print('\nh_2:\n',h_2)
#
# h_3 = h.var(axis = 0)
#
# print('\nh_3:\n',h_3)
#
# h_4 = h.var(axis = 1)
#
# print('\nh_4:\n',h_4)
#
#
# i = np.random.randn(1,100)
# print('i:\n', i)
#
# i_1 = i.mean(axis = 0)
#
# print('\ni_1:\n',i_1)
#
# i_2 = i.mean(axis = 1)
#
# print('\ni_2:\n',i_2)
#
# i_3 = i.var(axis = 0)
#
# print('\ni_3:\n',i_3)
#
# i_4 = i.var(axis = 1)
#
# print('\ni_4:\n',i_4)

# ---------- Onsdag 3
#
# N = 10
# for i in range(1,N+1):
#     print(i)
#
# #-
# print('----')
# a = [1, -1, 0, np.pi, np.sqrt(10), np.sin(2)]
#
# for i in a:
#     print(i)
#
# print('----')
# r = [[3,5,4], [8,6,7]]
#
# for i in r:
#     print(i)
#
#
# print('\nDouble:\n')
# for i in r:
#     for s in i:
#         print(s)
#


#-
#print('----')

# N_1 = 100
#
# x_1 = [1]
#
# for i in range(1,N_1+1):
#     x_1.append(.5*x_1[-1])
#
# #plt.plot(x,"ro")
# #plt.show()
#
#
# plt.semilogy(x_1, "ro")
# plt.show()

#Linear convergence towards 0

#-
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

#Super linear convergence towards 0

#-
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

#-
# --- READING AND WRITING DATA ---
# print('')
#
# data_file = np.genfromtxt(fname = 'data_1.txt', delimiter=',') #Vi henter fil fra samme mappe som python fil ligger i
#                                                                 #Hvordan indhentes data andetsteds fra?
# print('data_file:\n', data_file)
#
# print('\ntype(data_file):\n', type(data_file))
#
# data_file_2 = np.genfromtxt(fname = 'data_1.txt', delimiter=',', dtype = 'int32')
#
# print('\ndata_file_2:\n', data_file_2)
#
# #-
#
# data_file_noise1 = data_file + np.random.randint(1,11, size = data_file.shape)
#
# print('\ndata_file_noise1:\n', data_file_noise1)
#
#
# data_file_noise2 = data_file + np.random.rand() #Påvirker alle elementer med samme støj
#
# print('\ndata_file_noise2:\n', data_file_noise2)
#
# #print('test', data_file.shape)
#
# #data_file_noise3 = np.random.randn(data_file.shape) #<- Hvordan gøres dette uden eksplesit at specificerer 3,5 eller lignende
#
# #print('data_file_noise3:\n', data_file_noise3)
#
# # data_file_noise4 = data_file + np.random.randn(size = data_file.shape)
# #
# # print('data_file_noise4:\n', data_file_noise4)
#
# data_file_noise3 = data_file + np.random.randn(3,5) #<- Hvordan gøres dette uden eksplesit at specificerer 3,5 eller lignende
#
# print('\ndata_file_noise3:\n', data_file_noise3)
#
# data_file_noise4 = data_file + np.random.randn(3,5)
#
# print('\ndata_file_noise4:\n', data_file_noise4)
#
# np.savetxt('data_1noisy.csv', data_file_noise4)
#
# np.savetxt('data_1noisy2.txt', data_file_noise4, delimiter=';')


#!!!!!!!!!!!!!!!!!!!!! ------- SE også nedenstående fra Nicks programmeringstime i uge 3; - se også optaget øvelsestime i sig selv.
# import numpy as np
#
# #Skrive text fil
# file = open("testfile.txt", "w" ) #'w' for 'write'
#
# file.write("Hello World \n", )
# file.write("Dette er en text fil med text i.\n")
# file.write("Og dette er en linje mere.\n")
# file.write("Nu kan du åbne text filer.")
# file.close()
#
#
# print('--------------------------------------------------------')
# #Læse text fil
# print("Læs text file")
# file = open("testfile.txt", "r") #'r' for 'read'
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()
#
# print("for-løkker")
# file = open("testfile.txt", "r")
# for line in file:
#     print(line)
#
# print('--------------------------------------------------------')
# #gemme numpy array som text fil
# print("Gem array (intet at printe)")
# a = np.array([[1,2,3],[-1,0,1],[-3,-2,-1],[0.5,1.5,2.5]])
# np.savetxt('array2.txt',a,fmt='%f')
#
#
# print('--------------------------------------------------------')
# #Loade numpy arrays som text fil
# print("Printe gemte numpy arrays")
# K = np.loadtxt('array2.txt', usecols = range(0,3))
# print(K)
#
#
#
# print('--------------------------------------------------------')
# #mask numpy array
# print("mask arrays")
# mask = a > 0
# print(mask)
# print(a[mask])
#
# print('--------------------------------------------------------')
# #slice numpy array
# print("Slice array")
# print("-------")
# print("a =",a)
# a1 = a[0:2,0:2]
# print("-------")
# print("a1 =", a1)
# a2 = a[1:3,1:2]
# print("-------")
# print("a2=",a2)
#
# print('--------------------------------------------------------')
# print("printe numpy array helt standard (ekstra)")
# file = open("array2.txt", "r")
# for line in file:
#     print(line)
# file.close()
#
# print('--------------------------------------------------------')






#------------------------------------------------------------------
# Mandag 4

def f(x):
    return x**6 - x - 1

# x = np.linspace(1,1.3,num = 10^3)
# y = f(x)
#
# plt.figure #<-hvad gør figure?
# plt.plot(x,y)
# plt.axhline(0, color="black")
# plt.show()
#
#
# #----------
#
#
# a = 1.0
# b = 1.3
#
# eps = 10**(-8)
#
# numit = int(np.ceil((np.log(b-a)-np.log(eps))/np.log(2))) #for at vores c_n skal være epsilon tæt på konvergenspunktet r,
#                                                     # Ses at dette er tilfældet for n >= numit
# print('numit:', numit)
#
# K = False
#
# for i in range(1,numit + 1):
#     c = (a + b) / 2
#     test = f(a) * f(c)
#     if f(c) == 0:
#         print("c fundet ved iteration %s" %i, " med c = %s" %c)
#         print(i, c, b-a)
#         K = True
#         break
#     elif test<0:
#         b = c
#         print(i, c, b-a)
#     else:
#         a = c
#         print(i, c, b-a)
# if K == False:
#     print("Loop afsluttet efter %s iterationer" %numit, "bedste bud på c er c = %s" %c)


def BiSek(a, b, n, f, eps = 10^-8): #Bemærk at denne metode kun finder én rod
    #Få denne til at blive ved med at køre indtil at differensen er mindre end eps
    #<- men hvad skal vi så gøre af n????
    #<- Måske med en sådan: "Vi nåede ikke indenfor eps indenfor n iterationer" -
    # og så lader vi while loop køre til vi når indenfor epsilon.
    #<- Vi kunne også spørge "Vil du fortsætte søgningen "Ja/Nej" gennem brug af input funktionen,
    #som så registreres i en conditional, og hvis Ja, så køres der 100 iterationer mere...
    K = False
    n = int(n)
    print("i  ", "c   ", "b - a   ", "np.abs(b-a)-eps\n")
    for i in range(1,n + 1):
        c =  a + (b - a) / 2 #NI bog s. 76 siger denne form er bedre end c = (a+b)/2
        #test = f(a) * f(c) # NI bog s. 76 siger at det er bedre at bruge teststørrelsen np.sign(f(a)) != np.sign(f(c))
                            #I stedet for f(a)*f(c) < 0:
        test = np.sign(f(a)) != np.sign(f(c))
        if f(c) == 0:
            print("c fundet ved iteration %s" %i, " med c = %s" %c)
            print(i, c, b-a, np.abs((b-a)-eps))
            K = True
            break
        elif test == True:
            b = c
            print(i, c, b-a, np.abs((b-a)-eps))
        else:
            a = c
            print(i, c, b-a, np.abs((b-a)-eps))
    if K == False:
        print("Loop afsluttet efter %s iterationer" %n, "bedste bud på c er c = %s" %c)
    return(c)

# def f(x):
#     return x**6 - x - 1
#
# q = BiSek(1.0, 1.3, 25, f)

#!!!!!!!!!!!!!!!!! - Se generelt metoden implementeret i NI-bog s.76-78 - Den er ret nice



#-----------------
#Newton
print('')

def f(x):
    return x**6 - x - 1

def df(x): #Hvordan får vi Python til at differentierer? - se nedenfor
    return 6 * x**5 - 1

# N = 10
#
# #x_0 = 1.5 #Vores startgæt - !!! - Vi genbruger så meget som muligt så det går hurtigere ->
# x = 1.5
#
# for i in range(N+1):
#     x -= f(x) / df(x)
# print(x)
#
# print(f(x))

def Newtons(x, f, df, M = 100, delta = 10**(-10), eps = 10**(-8)):
    #Se Idéer til videreudvikling under BiSek funktionen

    #Hvad er det vi kommer tæt på? - Hvad skal vi måle eps i forhold til?
    #<-|x_n+1-x_n|<delta?

    M = int(M)
    print("k", "x_(k-1)             ", "x_k            ", "abs(x_(k-1)-x_k)")
    for k in range(1,M+1):
        z = x
        x = x - f(x) / df(x)
        if np.abs(z-x) >= delta and np.abs(f(x)) >= eps:
            print(k, z, x, np.abs(z-x))
        else:
            print(k, z, x, np.abs(z-x))
            print('\neps = {}, delta = {}.'.format(eps, delta))
            print('|f(x_{})| = {} < eps = {}.'.format(k,np.abs(f(x)),np.abs(f(x))<eps))
            print('|x_{} - x_{}| = |{} - {}| = {} < delta = {}.'.format(k, k-1, x, z, np.abs(x-z), np.abs(x-z) < delta))
            break
    return x

w = Newtons(1.5, f, df)
print(w)

#Bemærk at python også virker med komplekse tal i funktioner som eksempelvis f(x) osv....
print('')

# x_0 = complex(real = 0, imag = 1.2)
#
# w_1 = Newtons(x_0, f, df)
# print(w_1)
# print(np.abs(f(w_1)))

# Complex conjugate root theorem:

# "In mathematics, the complex conjugate root theorem states that if P
# is a polynomial in one variable with real coefficients, and a + bi is a
# root of P with a and b real numbers, then its complex conjugate a − bi is also
# a root of P".


#--------
print('')
#Differentation i python
#Symbolsk afledningen af relativt enkle funktioner kan ske ved;

# def Newtons2(f,x,M):
#   from sympy import diff,symbols
#   y = f(x)
#   w = symbols('w') #w er nu en variabel som kan være hvad som helst, og som derfor kan regnes med
#   df = diff(f(w), w)
#   z = x
#
#   for k in range(1,M+1):
#       z = z - y / df.subs(w,z)
#       y = f(z)
#       print(k,z,y)
#   return z
#
# print(Newtons2(f, 1.5, 12)) #Tager lige lidt længere tid pga. symbolske differentation.

#---- 4.3 Sekant metoden
# Ingen officiel implementering.



#-----4.4 Horners metode

# def f(x):
#     return x**6 - x - 1
#
#
# dim = 6
#
# coef = np.zeros(dim + 1)
#
# coef[6] = 1
# coef[1] = -1
# coef[0] = -1
#
# t = 2
#
# b = np.zeros(dim + 1)
# # c[0] not defined but easier indexation this way
# c = np.zeros(dim + 1)
#
# b[dim] = coef[dim]
# c[dim] = b[dim]
# # recall last bound is exclusive
# for k in range(dim-1, -1, -1):
#     b[k] = coef[k] + t * b[k+1]
#     c[k] = b[k] + t * c[k+1]
#
# print('values=', b[0], c[1])
#
# def horner(coef,t):
#     dim = coef.shape[0] - 1
#     b[dim] = coef[dim]
#     c[dim] = b[dim]
#     for k in range(dim-1, -1, -1):
#         b[k] = coef[k] + t * b[k+1]
#         c[k] = b[k] + t * c[k+1]
#     return b[0], c[1]
#
# print(horner(coef,2))






















































