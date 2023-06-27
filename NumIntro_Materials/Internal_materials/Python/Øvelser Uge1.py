#
import matplotlib.pyplot as plt
import math
import numpy as np


#Tips og tricks med pyCharm og python;
    #Pycharm;
        #Bemærk at hvis pyCharm er igang med at foreslå en kommando, vil CTRL+Q give dig en forklaring.
          #Bemærk hertil også, at hvis du er indenfor argumenterne af en kommando og bruger CTRL+Q
          #fås diverse dokumentation + link til yderligere dokumentation.
        #Shift+ESCAPE lukker "RUN"
        #CTRL+SPACE giver foreslag til autocomplete.
        #CTRL+SHIFT+ENTER afslutter automatisk ting der er mangler (eks. mangel på paranteser)

        #CTRL+SHIFT+ALT+7 Lav kommentar eller udkommentér udvalgte linjer

        #SHIFT+F10 kører de valgte linjer kode

#Spørgsmål til pyCharm og Python
    #PyCharm
        #HVORFOR VIRKER SHIFT+F10 ikke nær så godt som det skal?!!!!


    #Python

#CP 1.3.1;
#Vi tager inspiration fra Return value i tutorial hvor vi laver Fibonacci;

#----------------------------------
#def fib(n):
#    """This is documentation string for function. It'll be available by fib.__doc__()
#    Return a list containing the Fibonacci series up to n."""
#    result = []
#    a = 1
#    b = 1
#    while a < n:
#        result.append(a)
#        tmp_var = b
#        b = a + b
#        a = tmp_var
#    return result
#
#print(fib(10))
#---------------------------------

def seq27(n = 100, x_1 = 1, x_2 = 1-math.sqrt(3), abstjek = False):
    """This is documentation string for function. It'll be available by seq27.__doc__()
    Return a list containing the first n elements of the sequence defined in P1.3.27."""

    result = [x_1, x_2]
    print(x_1)
    print(x_2)
    q = 3
    while q <= n: # Får vi 100 eller kun 99 linjer? -
        tempsub1 = result[-1] #Henter umiddelbart tidligere element i følgen
        tempsub2 = result[-2] #Henter elementet der ligger to tidligere i følgen
        temp = 2*(tempsub1 + tempsub2) #Lægger de to hentede elementer sammen i det format følgen er defineret udfra
        print(temp) #Print hvert element i følgen
        result.append(temp) #Tilføj det nye element til result listen
        if (abstjek == True and (math.fabs(temp) >  math.fabs(tempsub1))): #Vi tjekker om den numeriske følge vokser
            print("Vi terminerer den numeriske følge, da absolutværdien vokser.")
            break
        q += 1 #Forhøj q med 1
    print("Antal elementer i result: %d" % len(result)) #Bruger metode fra Strings->Strings formatting
    return result

print(seq27(abstjek=True))

#Det viser sig at det går godt med den numeriske følge i et stykke tid, hvor den både skifter fortegn
# og konvergerer mod nul som den egentlige følge gør. - Vi retter koden så den inkluderer en tjek-conditional som
# lader os tjekke hvornår det begynder at gå galt. - Denne afsløre at det første gang går galt i følgeelement
# nummer 29, som har absolut værdi større end følgeelement nummer 28.

# Dette skyldes sandsynligvis computerberegningsfejl.

#??? Hvordan laver vi grafer over følger? - se sandsynligvis kapitel 3 i Numerisk analyse med python.pdf


#-----------------------------------------------------

#CP1.3.3 - #Se Hæfte
# a = (1 - 3**(100)) / (2**99) #Bemærk at vi ikke bruger ^ her!!!!
# print(a) #-8.131223550704305e+17

# def seqCP133(n = 100, x_0 = 0, x_1 = -2):
#     """This is documentation string for function. It'll be available by seqCP133.__doc__()
#     Return a list containing the first n elements of the sequence defined in CP1.3.3."""
#
#     result = [x_0, x_1]
#     print(x_0)
#     print(x_1)
#     q = 2 #Bemærk at vi starter ved 2, fordi næste skal være x_2 i dette tilfælde
#     while q <= n: #
#         tempsub1 = result[-1] #Henter umiddelbart tidligere element i følgen
#         tempsub2 = result[-2] #Henter elementet der ligger to tidligere i følgen
#         temp = (8 * tempsub1 - 3 * tempsub2) / 4 #Lægger de to hentede elementer sammen i det format følgen er defineret udfra
#         print(temp) #Print hvert element i følgen
#         result.append(temp) #Tilføj det nye element til result listen
#         q += 1 #Forhøj q med 1
#     print("Antal elementer i result: %d" % len(result)) #Bruger metode fra Strings->Strings formatting
#    return result
#
# a_2 = seqCP133(100, 0, -2)[-1]
# print(a_2)
# a_d = math.fabs(a-a_2)
# print("alsolut differens mellem seqCP133 og algebraiske udregnede: %d" % a_d) # 0 - voldsomt!



#CP1.3.4
#a)
#Se CP1.3.1

#b)
# beta = (1-math.sqrt(3))**(-1)
#
# N = 10**2+1
# values = []
# for n in range(1,N):
#     y_n = beta*(1-math.sqrt(3))**n
#     values.append(y_n)
#     print('Iteration ', n, ' y_n = ', format(y_n,'20.15f'))
# plt.plot(values, color='green', linestyle='dashed', marker='o',
#      markerfacecolor='blue', markersize=12)
# plt.title("Main Title", size = 25, rotation = 20)
# plt.suptitle("Superiour Title", color = "green")
# plt.xlabel("n = ")
# plt.ylabel("y_n")
# plt.grid(True)
# plt.show()

#c)
# Vi bemærker, at vi fra s.43 har at unit roundoff error
# def MachineEpsilonEst(redstep = 1/2):
#     epsilon = 1.0
#     while 1 + epsilon != 1:
#         print(epsilon)
#         epsilon = epsilon * redstep
#     print("Med det valgte reducerende trin", redstep, "har vi machine epsilon estimat på", epsilon)
#     return epsilon
# dredstep = 9999/10000
# qwew = MachineEpsilonEst(dredstep)
#
#
# alpha = qwew
# beta = (1-math.sqrt(3))**(-1)
#
# N = 10**2+1
# values2 = []
# for n in range(1,N):
#     z_n = alpha*(1 + math.sqrt(3))**n + beta * (1-math.sqrt(3))**n
#     values2.append(z_n)
#     print('Iteration ', n, ' z_n = ', format(z_n,'20.15f'))
# plt.plot(values2, color='green', linestyle='dashed', marker='o',
#      markerfacecolor='blue', markersize=12)
# plt.title("Main Title", size = 25, rotation = 20)
# plt.suptitle("Superiour Title", color = "green")
# plt.xlabel("n = ")
# plt.ylabel("z_n")
# plt.grid(True)
# plt.show()

#Denne stikker per python ret hurtigt afsted mod uendelig - Hvorfor???


#CP1.3.5 - #Se Hæfte
#Del 1: x_0 = 1, x_1 = pi

def seqCP135(n = 50, x_0 = 1, x_1 = np.pi):
    """This is documentation string for function. It'll be available by seqCP135.__doc__()
    Return a list containing the first n elements of the sequence defined in CP1.3.5."""
    result = [x_0, x_1]
    print(x_0)
    print(x_1)
    q = 2
    while q <= n: #
        tempsub1 = result[-1] #Henter umiddelbart tidligere element i følgen
        tempsub2 = result[-2] #Henter elementet der ligger to tidligere i følgen
        # x_(n+2)-(pi-pi^-1)*x_(n+1)+x_n = 0 <=> x_(n+2)=(pi-pi^-1)*x_(n+1)-x_n <=> x_m = (pi-pi^-1)*x_(m-1)-x_(m-2)
        temp = (np.pi + (np.pi)**(-1)) * tempsub1 - tempsub2 # Sammensætningen ovenfor.
        print('Iteration ', q, ' x_n = ', format(temp,'20.15f')) #Print hvert element i følgen
        result.append(temp) #Tilføj det nye element til result listen
        q += 1 #Forhøj q med 1
    plt.plot(result, marker='o', markerfacecolor='blue', markersize=12)
    plt.xlabel("n = ")
    plt.ylabel("x_n")
    plt.grid(True)
    plt.show()
    return result


x_50p = seqCP135(50, x_0 = 1, x_1 = math.pi)[-1]

# Vi løser nu differens ligningen manuelt. Vi gør dette ved brug af T1.3.1, og T1.3.2, og ser at p(l)=l^2-(pi+pi^-1)*l+1
# Vi får nogle ret komplicerede rødder på denne, men får den generelle løsning x_n = alpha * y^n + beta * z^n, for y,z
# værende rødder i p.
# -> Vi har y = (Pi^2 + 1 + sqrt(Pi^4 - 2*Pi^2 + 1))/(2*Pi),
# ->        z = (Pi^2 + 1 - sqrt(Pi^4 - 2*Pi^2 + 1))/(2*Pi)

#
# For n=0 fås x_0 = alpha * 1 + beta * 1 = alpha + beta, således at for x_0 = 1 vil vi kunne isolere så beta = 1 - alpha
# For n=1 fås efter reduktion at x_1 = alpha * y^1 + beta * z^1 = (alpha * pi^2 + beta)/pi, således at for x_1 = pi fås
# ved samtidig indsættelse af beta = 1 - alpha udledningen fra n = 0 - tilfældet; pi = (alpha * pi^2 + 1 - alpha) / pi
# <=> pi^2 = alpha * pi^2 + 1 - alpha
# <=> pi^2 - 1 = alpha * pi^2 - alpha
# <=> pi^2 - 1 = alpha * (pi^2 - 1)
# <=> (pi^2 - 1) / (pi^2 - 1) = alpha
# <=> alpha = 1
# => beta := 1 - alpha = 1 - 1 = 0, således at den generelle løsning bliver;
# x_n = alpha * y^n + beta * z_n = 1 * y^n + 0 * z_n = y^n = ((Pi^2 + 1 + sqrt(Pi^4 - 2 * Pi^2 + 1))/(2 * Pi))^n

# For n=50 fås (viser det sig) y_50 = pi^50 => x_n = y_n for n = 50; x_50 = y_50 = pi^50 - vi kan nu sammenligne x_50
# udregnet manuelt med dens python udregnede pendant, x_50p ved at finde den relative afrundingsfejl;
# abs((x_50 - x_50p)/x_50);

x_50 = (np.pi)**50

x_rd = math.fabs((x_50 - x_50p)/(x_50))
print("relative differens mellem x_50 og x_50p: %d" % x_rd) # 0 - voldsomt!
# - Hvis man giver Maple vores x_50 og stiller samme spørgsmål siger den; 6.525356153*10^(-9)

###################################################
#Del2; x_0 = 1, x_1 = 1/pi

# Tjek Del1 af spørgsmålet ovenstående :)
# Bemærk at vi fortsat har beta = 1 - alpha, hvorfra vi fortsat har ligningen;
# 1/pi = x_1 = (alpha(pi^2 - 1) + 1) / pi
# <=> 1 = alpha(pi^2 - 1) + 1
# <=> 0 = alpha(pi^2-1)
# (per 0-regel) => alpha = 0
# => beta = 1 - alpha = 1 - 0 = 1, således at x2_n = alpha * y^n + beta * z^n = 0 * y^n + 1 * z^n = z^n.

# For n = 50 fås dermed;
#x2_50 = z^50 = 1/(pi^50) <- som altså er det algebraiske "manuelle" "bud"

x2_50 = 1 / (np.pi**50)

#Vi lader Python om videre;
x2_50p = seqCP135(50, x_0 = 1, x_1 = 1/(np.pi))[-1]

x2_rd = math.fabs((x2_50 - x2_50p)/(x2_50))
print("relative differens mellem x2_50 og x2_50p: %d" % x2_rd) # 90399549442687751731002008928256 - voldsomt x 3!



#FORKLARING PÅ FORSKEL I DEL1 vs DEL2; !!!!!!!!!!!!!!!!!!!!!!!!:


