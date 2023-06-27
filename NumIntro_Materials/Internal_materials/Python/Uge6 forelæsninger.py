import numpy as np
import matplotlib.pyplot as plt
from math import pi

def checkwithReduceIfDuplicates(listOfElems, reduce = False):
    ''' Check if given list contains any duplicates '''
    uniqueListOfElems = list()
    for elem in listOfElems:
        if elem in uniqueListOfElems:
            if not reduce: # <=> if reduce == False:
                return True
        else:
            uniqueListOfElems.append(elem)
    if not reduce:
        return False
    else:
        return uniqueListOfElems

def Newton_HornerCoef(x,y, reduce = False):
    # Laver koefficienterne til Newton interpolation af x og y, dette gøres gennem brug af Horners metode
    cwrid = checkwithReduceIfDuplicates(x, reduce)
    if cwrid:
        if input("x contains duplicate values. - Do you want to use Newton_horner on the unique values? (Y/N)") in ["Y", "y","Yes","yes"]:
            x = np.array(checkwithReduceIfDuplicates(x, reduce = True), dtype = np.float64)
            print("The list of unique values of x is:\n{}".format(x))
        else:
            raise AttributeError("x has duplicate values that were selected to not be fixed, ending script now.")
    elif not cwrid:
        x = np.float64(x) # in principle "do nothing", as we seek the else condition to be all(\{True,False} encompassing
        # <- but just in case x is not float64, we might as well set it to be.
    else:
        x = np.array(cwrid, dtype = np.float64)
    N = len(x)
    C = np.zeros(N, dtype = np.float64) #initiering af vektor til
    C[0]=y[0]
    for k in range(1,N):
        d = x[k]-x[k-1]
        u = C[k-1]
        for i in range(k-2,-1,-1):
            a = x[k]-x[i]
            u = u*a+C[i]
            d=d*a
        C[k]=(y[k]-u)/d
    return C



def Newton_poly(x,C,t): #Træk koordinater fra Newton_Hornercoef?
    N = len(x)
    u = C[N-1]
    for i in range(N-2,-1,-1):
        a = t - x[i]
        u = u*a+C[i]
    return u

#Vi burde skabe en samlet funktion som både laver og bruger koefficienterne, tager funktionen f som input
# og får info om indeling og interval.


def f(x):
    return 1/(1+25*x**2)

dis = np.linspace(-1,1,20)
ydis = f(dis)

plt.plot(dis,ydis,'ro')
plt.title("Bindingspunkter for polynomiet")
plt.axhline(0, color = "black")
plt.show()

c = Newton_HornerCoef(dis,ydis)
cont = np.linspace(-1,1,10**3)
pcont = Newton_poly(dis,c,cont) #polynomiet baseret på koefficienterne c, og x-punkterne dis
#evalueret i punkterne fra cont

fcont = f(cont) #de rent faktiske funktionsværdier til de forskellige argumenter i cont

plt.plot(dis,ydis,'ro') #Plot af værdierne som binder polynomiet
plt.plot(cont,pcont, label = "Newton") #plot af de forskellige polynomieværdier
plt.plot(cont,fcont,label = 'f') #Plot af de forskellige funktionsværdier
plt.axhline(0, color = "Black")
plt.title("Bindingspunkter, funktionsværdier, og polynomiumsværdier ævkidistant [-1,1]")
plt.legend()
plt.show()

# Vi ser at vi har et N'te grads polynomium (=len(x)'te gradspolynomium), således at polynomiet
# rigtig gerne vil stikke afsted, og generelt bliver meget volatil som x bliver numerisk større
# hovedsageligt drevet af de største potensled.
### -> Hvis vi havde punkter som ikke lå ækvidistant, men i stedet for tættere på hinanden som x->+-1
# idet vi skaber vores polynomium, ville vi kunne tvinge en "pænere opførsel" af polynomiet som z->+-1

# Vi bruger de såkaldte Chebyshev-noder;

dis = np.linspace(-1,1,41)
n = len(dis)
ch_nodes = np.zeros(n)

for i in range(n):
    ch_nodes[i] = np.cos((i+0.5)*pi/n)

fch = f(ch_nodes)

plt.plot(ch_nodes,fch, 'ro')
plt.title("Chebychevnodes")
plt.axhline(0, color = "black")
plt.show()

c_ch = Newton_HornerCoef(ch_nodes, fch)

cont = np.linspace(-1,1,10**4)
pcont = Newton_poly(ch_nodes, c_ch, cont) #polinomieværdierne
fcont = f(cont)

plt.plot(ch_nodes,fch,'ro') #Plot af værdierne som binder polynomiet
plt.plot(cont,pcont, label = "Newton") #plot af de forskellige polynomieværdier
plt.plot(cont,fcont,label = 'f') #Plot af de forskellige funktionsværdier
#<- Hvorfor plottes ikke bare punkterne, men i stedet linjer mellem usynlige punkter?
#<- Bemærk dertil at dette er misvisende for f, fordi der faktisk foregår parvis
# lineær interpolation af f mellem fininddelingspunkterne lavet af cont!!!!

plt.axhline(0, color = "Black")
plt.title("{} bindingspunkter samt tilhørende funktions- og polynomiumsværdier, chebyshev [-1,1]".format(n))
plt.legend()
plt.show()

#Bemærk også at der er tale om "global interpolation" idet vi forsøger at interpolere f gennem Newton
# over hele intervallet [-1,1] med én interpolation, som i dette tilfælde er et polynomium lavet gennem
#Newton med brug af Horner.


############### Lav integreret interpolationsmetode!!!!
############### Hvordan laver vi selv chebychev nodes på andre intervalleer?
############### Lav symbolic printing af polynomiet

#Problem 6.1.22;
x = np.array([-2,0,1])
y = np.array([0,1,-1])

c = Newton_HornerCoef(x,y)
print(c)










