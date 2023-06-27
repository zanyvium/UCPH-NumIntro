"""
Dette er en python fil til dem som er interesseret i at se om deres skills i Python er "gode" nok.

I denne fil vil du blive bedt om at lave din egen kodning. Der vil være en prædefineret funktion. Denne funktion skal kunne returne den værdi som der bliver bedt om.
Hvordan programmet bliver skrevet og hvor optimeret det er, er op til dig.

Du vil kunne sende mig din python-fil med dit løsnings forslag. Min email er: vzm230@alumni.ku.dk
Hvis du ikke kan sende filen over der, kan du altid prøve min private mail: nickvillumlaursen@gmail.com

Du må selv om hvilke test du bruger til din kode. I.e du må selv vælge dine lister og værdier n,a,b. Så længde at din kode bare opfylder kriteriet som står over hver opgave.

Du må selv om hvordan du retunerer, så længe et resultat bare bliver returneret (Medmindre andet er skrevet).
"""

import numpy as np
import matplotlib.pyplot as plt

#Eksempel på en kode:
def Halver(n):

    if n<1:
        print("n for lille")
        return None
    k = 0
    i = 0
    while k<1:
        a = n/2
        if a%2 != 0:
            print(n, "er sidste tal i halverings rækken før du får et ulig tal")
            return n,i
        i = i+1
        n = a

Halver(2048)


#Lav en kode som summer alle de naturlige tal op til n.
def summe(n):

    #Indsæt egen kode her. Fjern None når du er færdig og indsæt i stedet resultatet.

    return None

#Lav en kode som multiplicer alle de naturlige tal op til n.
def gange(n):

    #Indsæt egen kode her. Fjern None når du er færdig og indsæt i stedet resultatet.

    return None

#Lav en kode som kan finde abselut værdien af et tal a.
def abse(a):

    #Indsæt egen kode her. Fjern None når du er færdig og indsæt i stedet resultatet.

    return None

#Lav en kode som tjekker om et tal a er et lige tal.
def Tjeklige(a):

    #Indsæt egen kode her. Hvis taller er et lige tal, så return True ellers return False.

    return None

#lav en kode som kan tjekke hvilket type objekt a er. Hvis man er modig kan man også få det til at printe dette objekt.
def type(a):

    #Indsæt egen kode her. Fjern None når du er færdig og indsæt i stedet resultatet.

    return None

#Lav en kode som tjekke om a er et primtal.
def prim(a):

    #Indsæt egen kode her. Fjern None når du er færdig og indsæt i stedet resultatet.

    return None

#Lav en kode som returnere et tal a's primfaktorisering. returner en liste med dens prim faktorisering.
def primfak(a):

    #Indsæt egen kode her. Fjern [] når du er færdig og indsæt i stedet resultatet.

    return []

#Lav en kode som retunere de to lister samlet sum, i.e c = [a_0+b_0, a_1+b_1, ..., a_n+b_n].
def listsum(a,b):

    #Indsæt egen kode her. Fjern [] når du er færdig og indsæt i stedet resultatet.
    return []

#Lav en kode som løser følgende rekursive ligning, rekusivt: x_n=2*x_{n-1}, hvor x_0=1. Vi ønsker kun at retunere det sidste tal.
def rek1(n):

    #Indsæt egen kode her. Fjern None når du er færdig og indsæt i stedet resultatet.

    return None

#Lav nu en kode som løser tidligere rekusive løsning, iterativt. vi ønsker kun at retunere det sidste tal.
def ite1(n):


    #Indsæt egen kode her. Fjern None når du er færdig og indsæt i stedet resultatet.

    return None

#Lav en kode som laver matrix sum af to numpy array's. Lav også et tjek for at tjekke at de to matricer har samme dimensioner.
def matrixadd(A,B):

    #Indsæt egen kode her. Fjern None når du er færdig og indsæt i stedet resultatet som er et numpy array.

    return None

#Lav en kode som har mere end to "funktioner af data" i sig. Derefter plot dem. Du skal ikke returne noget her.
def plot1(a : list,b : list):

    #indsæt egen kode her.


"""
Herved kommer nu nogle ekstra opgaver, som kræver at man skal tænke sig om. Altså ikke bare lave kode, men faktisk også tjekke om
den teori man nu "opfinder"/vælger at bruge, faktisk kan lade sig gøre.

"""

#Lav en kode som ordner en liste, i.e den sortere en liste fra mindste værdi til største værdi.
def sort(a):

    #Indsæt egen kode her. Fjern [] når du er færdig og indsæt i stedet resultatet som er en ordnet liste.

    return []

#Lav en kode som omdanner et decimal tal til et binær tal. Gør dette uden brug af funktioner til at omdanne tal.
def DecTODBi(a):

    #Indsæt egen kode her. Fjern None når du er færdig og indsæt i stedet resultatet som er et decimal tal.

    return None

