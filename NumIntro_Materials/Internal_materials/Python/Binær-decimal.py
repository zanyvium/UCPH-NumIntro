#Fra Decimal til binær
import math
import numpy as np

# Der er mindst to forskellige mulige fremgangsmåder;
# 1;
    # Vi kan vælge at bruge tempk = np.floor(np.log(remainder)/(np.log(2))) til at finde den næste eksponent til 2, og
    # parre dette med remainder = x-np.sum(2**expo) for dermed at få de forskellige eksponenter og dermed også expo

# def DecBin(x):
#
#     result = []
#     expo = []
#     remainder = x
#
#     tempk = np.floor(np.log(remainder)/(np.log(2))) # Vi finder k så 2^k>x vil log(2^k)=k*log(2)>log(x) <=> k>log(x)/log(2)
#     result.append(1)
#     expo.append(tempk)
#     remainder = x-np.sum(2**expo)
#
#     while x-np.sum(2**expo) != 0:
#         remainder = x-np.sum(2**expo)
#         if remainder > 2**(tempk - 1):
#             result.append(1)
#             expo.append(tempk - 1)
#         elif 2**(tempk - 1) == remainder:
#             result.append(1)
#             expo.append(tempk - 1)
#             #break #Terminate while loop - we've found our binary expansion. - while x-np.sum(2**expo) != 0 giver dette automatisk?
#         #Hvis
#        tempk -= 1
def ListToThePower(my_list, b=2):
    return [ b**x for x in my_list ]
    #qwe[:] = map(lambda x: 2**x, qwe) #Dette er anden mulighed #??? <- hvad dælan gør lambda her?


def DecBinExpo(x):

    expo = []
    remainder = x
    tempk = np.floor(np.log(remainder)/(np.log(2))) # Vi finder k så 2^k>x vil log(2^k)=k*log(2)>log(x) <=> k>log(x)/log(2)
    expo.append(tempk)

    print('Remainder number %s is ' %len(expo), remainder)
    print('tempk number %s is ' %len(expo), tempk)
    print('')

    while x-np.sum(ListToThePower(expo)) != 0:
        print("inside")
        remainder = x-np.sum(ListToThePower(expo))
        tempk = np.floor(np.log(remainder)/(np.log(2)))
        expo.append(tempk)

        print('Remainder number %s is ' %len(expo), remainder)
        print('tempk number %s is ' %len(expo), tempk)
        print('')
    print(expo)
    return expo

def CountLen(x, q = 1):
    if q == 1:
        x[:] = map(lambda x: max(x,0), x)
        print("Positiv liste;", x)
    elif q == -1:
        x[:] = map(lambda x: min(x,0), x)
        print("Negativ liste;", x)
    return x


#Virker ikke særligt godt
CountLen(DecBinExpo(18))
qrt = DecBinExpo(119.3)



def DecBinBin(x):
    expo = DecBinExpo(x)
    binlen = np.abs(expo[0]-expo[-1])
    return binlen #lige nu eksporterer vi binlength. Dette er ikke enderesultatet. vi rengner binlen for at finde ud af
                    #hvor mange tal der skal være i decimal ekspansionen af x
                    # binlen virker for 119, og 119.3, men ikke for 18
                        # - der mangler en max{abs(expo[0]-expo[-1], expo[0]-0} hvis expo[0] og expo[-1] er positive
                        # og en min for negative
                    # En løsning er at tælle hvad det største positive tal er og lægge det til det største negative tal




