import numpy as np

#På intet tidspunkt blev en 'visual debugger' brugt. - lær sku også lige dette.

# 6.3;
# -  -  -  Oprindelig opstilling;
# ’ ’ ’
# Problemstatement : Given a postive integer x list all
# even numbers from zero and up to and including x
# ’ ’ ’
#:#

# x = 10
# for i in range(x):
#     if (i % 2) == 0:
#         print("FAULTY found even number = ", i)

#:#
# ______ Rettet opstilling;
# Vi bemærker at indeks i python er fucked så vi skal arbejde ekstra meget for at fikse shit
# Vi laver derfor følgende fiks for at løse problemopstillingen ordentligt

# x = 10
# for i in range(0, x + 1):
#     if (i % 2) == 0:
#         print('FIXED found even number = ', i)

# 6.4
# -  -  -  Oprindelig opstilling;
# ’ ’ ’
# Example of assigning an integer expression to a variable
# ’ ’ ’
#:#

# myVar = 5
# b = (((myvar*2)+3)*2)/3

#:#

# ______ Rettet opstilling;
# Navnet på variablen er 'myVar' - altså med stort 'V', der er skrevet 'myvar' - altså med lille 'v'
# Da variabelnavne er 'case-sensitive' ved Python ikke hvad myvar er for noget.
# Vi skriver derfor med stort V;

# myVar = 5
# b = (((myVar*2)+3)*2)/3
#
# print(b)
#
# # Alternativt, hvis opgavebeskrivelsen skal fortolkes i formatet 'lav b til int-værdi;
# print('---------')
#
# myVar = 5
# b = (((myVar*2)+3)*2)/3
# b_int = int(b)
# b_floor = np.floor(b)
# b_ceil = np.ceil(b)
#
# print('Værdierne b, b_int, b_floor, b_ceil\n', b, b_int, b_floor, b_ceil)
#
# print('Data typer af b, b_int, b_floor, b_ceil\n', type(b), type(b_int), type(b_floor), type(b_ceil))

# 6.5
# -  -  -  Oprindelig opstilling;
# ’ ’ ’
# Example of using float values. A float number is not the
# same as a real number. A float has finite precision.
# This means that a real number often will be ’ truncated ’
# or ’ rounded ’ when used in computations or displayed.
# This example helps illustrate some of the quirks when
# working with floatingpoint values.
# If we take a small number and continously try to make it
# even smaller then we will get to zero
# ’ ’ ’

# : #
# a = 1.97626258336e-323
#
# print(a)
# for x in range(10):
#     a = a / 2
#     print(a)

# : #

# ______ Rettet opstilling;
# Hvordan kan vi rette? - Vi har vel et underflow?
# a = float(1.97626258336e-323, dtype = 'float64') #<- Dette virker heller ikke lige for mig i dag...


# 6.6
# -  -  -  Oprindelig opstilling;
# ’ ’ ’
# Example of using float values. A float number is not
# the same as a
# real number. A float only has finite precision.
# This means that a real number will often be ’ rounded ’
# when used
# in computations or displayed.
# ’ ’ ’

# : #

# a = 1.97626258336e+307
# print(a)
# for x in range(10):
#     a = a * 2
#     print(a)


# : #

# ______ Rettet opstilling;
# Igen - Hvordan retter vi lige dette?


#

# 6.6
# -  -  -  Oprindelig opstilling;
# '''
# How small a floatingpoint number can we add to the value
# 1.0 and still get the value 1.0?
# '''

# : #

# epsilon = 1.0
# while (1.0 + 0.5 * epsilon) != 1.0:
#     epsilon = 0.5 * epsilon
# print("Approximated machine epsilon =", epsilon)


# : #

# ______ Rettet opstilling;
# En "fejl" kunne evt. være at der tages meget store trin nedad idet vi forsøger at estimerer 'machine epsilon'
# \equiv 'unit roundoff error' - Vi kan dermed tage mindre skridt, eksempelvis har vi i CP 1.3.4c) lavet følgende;

# : #


# # Vi bemærker, at vi fra s.43 har at unit roundoff error
# def MachineEpsilonEst(redstep = 1 / 2):
#     epsilon = 1.0
#     while 1 + epsilon != 1:
#         print(epsilon)
#         epsilon = epsilon * redstep
#     print("Med det valgte reducerende trin", redstep, "har vi machine epsilon estimat på", epsilon)
#     return epsilon
#
#
# dredstep = 9999 / 10000
# qwew = MachineEpsilonEst(dredstep)

# : #


# 6.8
# -  -  -  Oprindelig opstilling;
# '''
# '''

# : #

# x = 0.0
# for i in range(10):
#     x = x + 0.1
# if x == 1.0:
#     print(x, ' = 1.0')
# else:
#     print(x, ' <> 1.0')

# : #


# ______ Rettet opstilling;
# Lad os først lige se hvad der sker i loopen;
# : #
# x = 0.0
# for i in range(10):
#     x = x + 0.1
#     print(x)
# if x == 1.0:
#     print(x, ' = 1.0')
# else:
#     print(x, ' <> 1.0')

# - Ergo er 0.7 + 0.1 = 0.7999999999 af en eller anden grund
# Vi forsøger at tvinge 64 bit;

# x = np.float64(0.0)
# for i in range(10):
#     x = np.float64(x + np.float64(0.1))
#     print(x)
# if x == 1.0:
#     print(x, '= 1.0')
# else:
#     print(x, '<> 1.0')


# <- Ergo hjælper dette ikke - dette giver også mening,
# idet det sandsynligvis er en afrundings, og ikke bit-længde fejl

# Vi prøver derfor med en epsilon metode
# def isequalmethod(x, y, eps=10 ** (-8)):
#     return np.abs(x - y) <= eps
#
# x = 0.0
# for i in range(10):
#     x += 0.1
#     print(x)
# if isequalmethod(x, 1, eps = 10**(-8)):
#     print('x ~= 1.0')
# else:
#     print('x !~= 1.0')

# -> Alternativt kan man måske evt bruge np.sum eller lignende?


# : #


# 6.9
# -  -  -  Oprindelig opstilling;

# '''
# Given positive integer x find largest
# positive integer z such that z * z <= x.
# We call z the " integer " root of x.

# '''

# : #
# x = 39
# for z in range(x):
#     y = z*z
#     if y > x:
#         print ("Integer root of", x, "is", z-1)
# : #


# ______ Rettet opstilling;
# Overstående virker fint nok, man glemmer bare at stoppe;

# : #
# x = 39
# for z in range(x):
#     y = z*z
#     if y > x:
#         print("Integer root of", x, "is", z-1)
#         break #<- så stopper vi

# : #

# 6.10
# -  -  -  Oprindelig opstilling;

# '''
# Given positive integer x find largest
# positive integer z such that z * z <= x.
# We call z the " integer " root of x.

# '''

# : #

# x = 39
# for z in range(x):
#     y = z*z
#     if y > x:
#         print("Integer root of", x, "is", z-1)
#     break

# : #


# ______ Rettet opstilling;
# Samme løsning som i 6.9: - i dette tilfælde er der fejl i indentationen
#

# : #

# x = 39
# for z in range(x):
#     y = z*z
#     if y > x:
#         print("Integer root of", x, "is", z-1)
#         break #<- så stopper vi

# : #


# 6.11
# -  -  -  Oprindelig opstilling;
# '''
# Given positive integer a compute the
# value of the square of a using only the addition
# operator

# '''

# : #
# a = 5
# b = 1
# for i in range(a):
#     print(b)
#     b = b + a
# print("The square of", a, "is", b)

# : #


# ______ Rettet opstilling;
# !!
# #Forsøg 1:
# a = 9
# b = 1
# for i in range(a):
#     print(b)
#     b = b + a
# print("The square of", a, "is", b)

# !!

# Bemærk at denne metode næsten virker idet vi betragter differensligningen b_n = b_(n-1) + a
# => b_n = (b_(n-2) + a) + a = b_(n-2) + 2 * a => b_n = b_(n-q) + q * a => b_n = b_0 + n * a
# og da b_0 = 1 haves b_n = 1 + n * a ---- - Og hvorfor skulle dette relaterer sig til a^2 kan man tænke
# Det viser sig at vi ikke har ethvert tilfældigt n i spil: Vi kører jo denne process igennem
# for i = 0, 1, 2, 3, 4, 5, ..., a-1 -> ergo a-gange, så vi betragter et n = a ->
# Ergo fås at b_a = 1 + a * a = 1 + a^2 - Ergo må vi lige trække 1 fra til sidst.

# <- Der er dog problemer i det format at denne metode kun virker på positive tal
# <- ??? - Hvorfor?

# : #
# a = 5
# b = 1
# for i in range(a):
#     print(b)
#     b = b + a
# b += -1
# print("The square of", a, "is", b)

# -
# - Vi forbedre denne, ved at gøre det til en funktion;
# def badsqbyadd(a):
#     b = 1
#     for i in range(a):
#         b = b + a
#     b += -1
#     print("The square of", a, "is", b)
#     return b


# q = np.arange(-5, 6)
# ql = []
# for i in q:
#     ql.append(badsqbyadd(i))
#
# print(ql)  # Vi ser at der er problemer med negative tal <- HVORFOR????


# Vi kan dog lave et dirty fix da (-a)^2 = a -> ergo kan vi i stedet for at forholde os til
# årsagen af problemet bare konkluderer at løsningen findes lettere end problemet;

# def badsqbyaddall(a):
#     a = np.abs(a)
#     return badsqbyadd(a)
#
#
#
# q2 = np.arange(-5, 6)
# ql2 = []
# for i in q2:
#     ql2.append(badsqbyaddall(i))
#
# print(ql2)

# Vi finder dertil hurtigt ud af, at der ingen grund er til at have b-ledet med,
# da vi netop søger b_n = a^2, i n=a ledet. -> se 6.12

# : #


# 6.12
# -  -  -  Oprindelig opstilling;
# '''
# Given positive integer a compute the
# value of the square of a using only the addition
# operator

# '''

# : #
# a = 5
# b = 0
# for i in range(a)
#     b = b + a
# print("The square of", a, "is", b)

# : #


# ______ Rettet opstilling;
#Vi skal huske kolon i slutningen af en for-linje.

# : #
# a = 5
# b = 0
# for i in range(a):
#     b = b + a
# print("The square of", a, "is", b)

# : #


# 6.13
# -  -  -  Oprindelig opstilling;
# '''


# '''

# : #
# a = 5
# b = 0
# for i in range(a):
#     b = b + a
# print ("The square of, a, "is", b)

# : #


# ______ Rettet opstilling;
#Vi mangler bare en afsluttende ' " ' efter 'of'
# : #
# a = 5
# b = 0
# for i in range(a):
#     b = b + a
# print("The square of", a, "is", b)
