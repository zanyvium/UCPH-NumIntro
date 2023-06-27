import numpy as np
import matplotlib.pyplot as plt

# -
# 1. Newtons metode fra pseudokode


# -
print('')
# 2. BiSektion med stop
# -Se forelæsnings python dokument - se også Pseudokode i bogen s. 76
# Følgende er hvad jeg allerede har;
# : #

# def BiSek(a, b, n, f, eps = 10^-8): #Bemærk at denne metode kun finder én rod
#     #Få denne til at blive ved med at køre indtil at differensen er mindre end eps
#     #<- men hvad skal vi så gøre af n????
#     #<- Måske med en sådan: "Vi nåede ikke indenfor eps indenfor n iterationer" -
#     # og så lader vi while loop køre til vi når indenfor epsilon.
#     #<- Vi kunne også spørge "Vil du fortsætte søgningen "Ja/Nej" gennem brug af input funktionen,
#     #som så registreres i en conditional, og hvis Ja, så køres der 100 iterationer mere...
#     K = False
#     n = int(n)
#     print("i  ", "c   ", "b - a   ", "np.abs(b-a)-eps\n")
#     for i in range(1,n + 1):
#         c =  a + (b - a) / 2 #NI bog s. 76 siger denne form er bedre end c = (a+b)/2
#         #test = f(a) * f(c) # NI bog s. 76 siger at det er bedre at bruge teststørrelsen np.sign(f(a)) != np.sign(f(c))
#                             #I stedet for f(a)*f(c) < 0:
#         test = np.sign(f(a)) != np.sign(f(c))
#         if f(c) == 0:
#             print("c fundet ved iteration %s" %i, " med c = %s" %c)
#             print(i, c, b-a, np.abs((b-a)-eps))
#             K = True
#             break
#         elif test == True:
#             b = c
#             print(i, c, b-a, np.abs((b-a)-eps))
#         else:
#             a = c
#             print(i, c, b-a, np.abs((b-a)-eps))
#     if K == False:
#         print("Loop afsluttet efter %s iterationer" %n, "bedste bud på c er c = %s" %c)
#     return(c)

# def f(x):
#     return x**6 - x - 1
#
# q = BiSek(1.0, 1.3, 25, f)

# : #
# -
print('')


# Vi følger pseudokode på s. 76

def BiSekPseudo(a, b, f, N = 100, delta = 10**(-10), eps = 10**(-8)):
    u = f(a)
    v = f(b)
    e = b - a
    print('a = %s' % a, ' | b = %s' % b, ' | u = %s' % u, ' | v = %s' % v)
    if np.sign(u) == np.sign(v):
        print("Invalid interval da fortegn af f ikke er forskelligt i a og b")
        return None
    for k in range(1, N + 1):
        e = e / 2
        c = a + e
        w = f(c)
        print('k = %s' % k, 'c = %s' % c, ' w = %s' % w, 'e = %s' % e)
        if np.abs(e) < delta or np.abs(w) < eps:
            break #stopkriterie - Kan muligvis gøres bedre - Se sekant
        if np.sign(w) != np.sign(u):
            b = c
            v = w
        else:
            a = c
            u = w
    return c

def f(x):
    return x**6 - x - 1

q = BiSekPseudo(1.0, 1.3, f)



# -
print('')
# 3. Sekant metode
def Sekant1(a, b, f, N = 100, delta = 10**(-10), eps = 10**(-8)):
    #Vi printer som at a = x_0, b = x_1 til at starte med.
    print('n = 0', 'x_0 = %s' %a, ' f(x_0) = %s' %f(a))
    print('n = 1', 'x_1 = %s' %b, ' f(x_1) = %s' %f(b))
    for n in range(2,N+1):
        if np.abs(f(a)) > np.abs(f(b)):
            a,b = b,a #Vi bytter a og b, hvormed f(a) og f(b) også bytter
        s = (b-a)/(f(b)-f(a))
        b = a
        a = a - f(a) * s
        print('n = %s' % n, 'x_%s' %n, "= %s" %a, ' f(x_%s) ' %n, "= %s" %f(a))
        if np.abs(f(a)) < eps or np.abs(b-a) < delta:
            print('\neps = {}, delta = {}.'.format(eps, delta))
            print('|f(x_{})| = {} < eps = {}.'.format(n,np.abs(f(a)),np.abs(f(a))<eps))
            print('|x_{} - x_{}| = |{} - {}| = {} < delta = {}.'.format(n, n-1, a, b, np.abs(b-a), np.abs(b-a) < delta))
            break
    return a

#Lav Sekant uden funktionskald hele tiden - se Pseudokode!!!!

def f(x):
    return x**2 - 2

Sekant1(0,1,f)
print('')
Sekant1(1,0,f)

#- -----------------------
print('')
#U4 O2;
#Se hæfte.
#Se også Example 1 side 75
#Vi bruger Newtons metode som udviklet i forbindelse med forelæsningerne og ikke øvelserne :(:(:(
def abphi(t):
    return np.sqrt(t ** 2 + (np.log(t)) ** 2)

def dabphi(t):
    return (t ** 2 + np.log(t)) / (np.sqrt(t ** 2 + (np.log(t)) ** 2) * t)



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
            print('x_{} = {}'.format(k,x))
            break
    return x

w = Newtons(1/2, abphi, dabphi, eps=10**(-5)) #eps = 10**-5 burde garanterer fem decimaler præcision?
#<- der går noget gal - vi tager logaritmer af negative værdier -
# hvor kommer de negative værdier dog fra?

#- Det lader til at være rigtige udregninger når der tjekkes med Geogebra. -<- Hvad er fejl så?
#<- SE GEOGEBRA!!!!!!

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!--------!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#<-Se hæfte for løsning til problemet; - Vi ser bort fra kvadratroden i afstandsfunktionen.


#Hvordan til fem decimaler præcist?

#-
print('')
#U4,O3;
# ... f(x) = 0 => x = pi... f(pi) = 0, f'(pi)\ne 0 (pi er simpel rod)...
def f(x):
    return x-np.pi

def df(x):
    return 1


Newtons(1,f,df, eps = 10**(-10))
#Skal vi så afrunde til ti decimaler??? - HVORDAN?

#Alternative funktioner kan også bruges - eksempelvis siges det at pi
# har lidt med cirkler at gøre, hvilket de trigonometriske funktioner også har.
# - Eksempelvis vil sin(pi) = 0 så f(x) = sin(x) er også en mulighed.





#-
print('')
#U4,O4:



















