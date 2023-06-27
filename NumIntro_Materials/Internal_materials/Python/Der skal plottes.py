#http://matplotlib.org/api/index.html
#http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot

############

######## Andre plotfunktioner;
import matplotlib.pyplot as plt
import numpy as np
fig, axes = plt.subplots(1,3, figsize = (12,4)) #Hvad dælan gør 'fig,' ?
x = np.arange(1,11)
axes[0].plot(x, x**3, 'g',lw=2)
axes[0].grid(True)
axes[0].set_title('default grid')
axes[1].plot(x, np.exp(x), 'r')
axes[1].grid(color='b', ls = '-.', lw = 0.25)
axes[1].set_title('custom grid')
axes[2].plot(x,x)
axes[2].set_title('no grid')
fig.tight_layout()
plt.show()






########




import matplotlib.pyplot as plt
N = 10
values = []
for n in range(1,N):
    x_n = (n+1)/n**2
    values.append(x_n)
    #print('Iteration ',n, ' x_n = ', format(x_n,'20.15f'))
#plt.plot(values)
#plt.show()

#
plt.plot(values, "ro")
plt.show()

#
plt.plot(values, "or") #Se dokumentation i de øverste links ("or"="ro")
plt.show()

#
plt.plot(values ,'b-')
plt.show()

#
plt.plot(values ,'gx')
plt.show()

#
plt.plot(values ,'m-')
plt.show()

#
plt.plot(values ,'r-.x')
plt.show()

#
# plt.plot(values, color='green', linestyle='dashed', marker='o',
#      markerfacecolor='blue', markersize=12)
# plt.show()



# #Ret gennemgående plot;
# plt.plot(values, color='green', linestyle='dashed', marker='o',
#      markerfacecolor='blue', markersize=12)
# plt.title("Main Title", size = 25, rotation = 20)
# plt.suptitle("Superiour Title", color = "green")
# plt.xlabel("X axis label")
# plt.ylabel("Y axis label")
# plt.grid(True)
# plt.show()

#Ret gennemgående plot2;
# print(*values[max(-11, -len(values)): -1], sep = "\n") # Det at sætte '*' før variablen, og sep = "\n" giver nye linjer.
#                                                         # - Giver det samme resultat som hvis vi printede med for-loops.
# plt.plot(values, color='green', linestyle='dashed', marker='o',
#      markerfacecolor='blue', markersize=12)
# plt.title("Main Title", size = 25, rotation = 20)
# plt.suptitle("Superiour Title", color = "green")
# plt.xlabel("X axis label")
# plt.ylabel("Y axis label")
# plt.grid(True)
# plt.show()



#!!!################!!!#   # Try writing a Python program to analyze the sequence equation x_n =(1+1/n)^n n>=1
#
# N2 = 10**3+1
# values2 = []
# for n in range(1,N2):
#     x_n2 = (1+1/n)**n
#     values2.append(x_n2)
#     #print('Iteration ', n, ' x_n2 = ', format(x_n2,'20.15f'))
# plt.plot(values2, color='green', linestyle='dashed', marker='o',
#      markerfacecolor='blue', markersize=12)
# plt.title("Main Title", size = 25, rotation = 20)
# plt.suptitle("Superiour Title", color = "green")
# plt.xlabel("X axis label")
# plt.ylabel("Y axis label")
# plt.grid(True)
# plt.show()

#Ligner sku noget konvergens mod naturlige ekspotentialfunktions grundtal.


#!!!################!!!#   # Write a program to analyze the sequence x_0=0.9, x_n=x_(n-1)^2, n>=1

# N3 = 15
# x_0 = 0.9
# values3 = [x_0]
# for n in range(1,N3):
#     temp = values3[-1]
#     x_n3 = temp**2
#     values3.append(x_n3)
#     print('Iteration ', n, ' x_n3 = ', format(x_n3,'20.15f'))
# plt.plot(values3, color='green', linestyle='dashed', marker='o',
#      markerfacecolor='blue', markersize=12)
# plt.title("Main Title", size = 25, rotation = 20)
# plt.suptitle("Superiour Title", color = "green")
# plt.xlabel("X axis label")
# plt.ylabel("Y axis label")
# plt.grid(True)
# plt.show()

#Den går ret hurtigt til 0.


