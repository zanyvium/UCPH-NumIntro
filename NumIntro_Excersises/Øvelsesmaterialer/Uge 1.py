#Starter med standard import
import numpy as np
import matplotlib.pyplot as plt

#Opgave 1

#Vi starter med at definere at vi vil lave en funktion. Dette gøres med koden "def". Derefter kalder vi koden noget, i.e "sol1", og derfra indsætter vi hvilken variabler den vil have, i.e (n). Afslut med :
def sol1(n):
    #Vi starter med at lave en liste B. Denne liste vil indeholde vores start værdier x_0 og x_1
    B = [1, 1-np.sqrt(3)]

    #Vi laver nu en for-løkke som vil gå fra 2 til n. Hvilket specifikt indeks vi er i, bliver noteret som $i$ i løkken.
    for i in range(2,n):
        #Vi beregner nu vores differens ligning. Vi k til at være den specifikke beregnet værdi.
        k = 2 * (B[i-1] + B[i-2])
        #Vi sætter nu denne værdi in i vores liste.
        B.append(k)
    #Herfra vil for-løkken nu gå fra $i$ til $i+1$ og begynde forfra. Dette vil den gøre til vi er færdig, i.e vi har ramt vores n-værdi

    #Herved laver vi nu vores plot. Vi starter med ylim for at give et limit på vores y-linie. Dette gøres bare for at i kan se hvordan denne commando fungerer
    plt.ylim(-1,80)

    #Herved vælger vi nu vores hvad vi vil plotte. Vi skriver efter ,"go" for at vi kan få et plot som ikke er med linier men med punkter.
    plt.plot(B,"go")

    #Nu giver vi titler til henholdsvis titlen, x-aksen og y-aksen
    plt.title("Opgave 1")
    plt.xlabel("Indeks n")
    plt.ylabel("Rekursive værdi")

    #Nu siger vi at, koden til dette plot skal vises.
    plt.show()

    #Vi Returner B i tilfælde af at vi skal bruge den. I skal ikke tænke så meget over return. Dette vil blive gennemgået senere i kurset.
    return B

#Nu vælger vi at køre koden. Dette gøres ved at "kalde" koden (CALL). Vi skriver altså hvad vores funktion hedder "sol1" og derefter indsætter vi det ønskede for hvad $n$ skal være., i.e 50.
sol1(50)


#For opgave 3 og 4.a) er det den samme process som går igennem. Igen ekstra forklaring behøves her.

#Opgave 3
def sol3(n):
    B=[0, -2]

    for i in range(2, n+1):
        k = 2 * B[i-1] - (3 / 4) * B[i-2]
        B.append(k)

    plt.plot(B,"go")
    plt.title("Opgave 3")
    plt.xlabel("Indeks n")
    plt.ylabel("Rekursive værdi")
    plt.show()
    #print(B[n-1])
    return B

sol3(100)

#Opgave 4

# a)
def sol4a(n):
    B = [1, 1-np.sqrt(3)]

    for i in range(2,n+1):
        k = 2 * (B[i-1] + B[i-2])
        B.append(k)

    plt.plot(B,"go")
    plt.title("Opgave 4.a")
    plt.xlabel("Indeks n")
    plt.ylabel("Rekursive værdi")
    plt.show()
    return B



#Koden for 4.b) er lidt anderledes. I denne kode laver vi en tom liste, da vi ikke har start værdier. Derfra insættes alle vores beregnede værdier i listen.
# b)
def sol4b(n):
    #Vi definer beta som er kendt fra opgave 1.3.27
    beta = (1 - np.sqrt(3))**(-1)
    B = []

    for i in range(0,n+1):
        k = beta * (1 - np.sqrt(3))**i
        B.append(k)

    plt.plot(B,"go")
    plt.title("Opgave 4.b")
    plt.xlabel("Indeks n")
    plt.ylabel("Rekursive værdi")
    plt.show()
    return B


"""
For c) skal vi igen lave en anden algoritme. Som jeg viste til øvelsen, så kan man finde hvad sin egens computer roungoff error er. Dette gøres i funktionen URE().
Vi bemærker at vi ikke behøver variabler i denne funktion. Dette er fordi vores funktion ikke bruger nogen variabler i sin algoritme.
"""

# c)
#Unit roundoff error af min computer
def URE():
    epsilon = 1.0

    while 1.0 + 0.5 * epsilon != 1.0:
        epsilon = 0.5 * epsilon
    print("Unit Roundoff Error:")
    print(epsilon)
    print("--------------------------------------------------------------")

    #Her er det vigtig at vi returner vores udregnet værdi. Dette vil blive forklaret i den næste funktion.
    return epsilon

#Selve løsningen
def sol4c(n):
    #Vi sætter alpha til at være li med URE(). Dette betyder at alpha er li den udregnet epsilon fra tidligere funktion. Hvis vi ikke returnede vores epsilon der, så vil vi ikke kunne gøre dette trik.
    alpha = URE()
    beta = (1 - np.sqrt(3))**(-1)
    B = []

    for i in range(0,n+1):
        k = alpha * (1 + np.sqrt(3))**i + beta * (1 - np.sqrt(3))**i
        B.append(k)
    plt.plot(B,"go")
    plt.title("Opgave 4.c")
    plt.xlabel("Indeks n")
    plt.ylabel("Rekursive værdi")
    plt.show()
    return B

#Herved kører vi nu opgave 4 a)-c).
sol4a(100)
sol4b(100)
sol4c(100)


#opgave 5 er også lidt anderledes. Den vil have at vi udregner den relative fejl. Se slides fra uge 1 onsdag
#Opgave 5
def sol5a(n):
    B = [1, np.pi]

    for i in range(2,n+1):
        k = (np.pi + (np.pi)**(-1)) * B[i-1] - B[i-2]
        B.append(k)

    #Vi finder valuen $\pi^{50}$.
    value = np.pi**n

    #Vi beregner nu vores relative fejl mellem vores value $\pi^{50}$ og vores beregnet $\pi^{50}$.
    RelativeError = (value-B[n]) / (value)

    #Vi printer så vores relative fejl.
    print("Relativ Fejl i a):")
    print(RelativeError)
    print("--------------------------------------------------------------")
    return RelativeError

sol5a(50)

#Opgave 5 b) er det samme stykke kode. Her skal vi i stedet for $p^{50}$ kigge på $\pi^{-50}$.

#Opgave 5
def sol5b(n):
    B = [1, np.pi**(-1)]

    for i in range(2,n+1):
        k = (np.pi + (np.pi)**(-1)) * B[i-1] - B[i-2]
        B.append(k)

    # Det skulle gerne give pi^50
    value = np.pi**(-n)
    RelativeError = (value-B[n]) / (value)

    print("Relativ Fejl i b):")
    print(RelativeError)
    return RelativeError

sol5b(51)


#Bare et sjovt eksempel på computeren ikke kan regne.
"""
def test():
    a = 1.0
    print(a)
    for i in range(10):
        a = a - 0.1
        print(a)

test()
"""
