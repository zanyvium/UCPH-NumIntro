import numpy as np
import matplotlib.pyplot as plt

def seqmaker(n):
    return (-1)**n/(2**n)

def summaker(st, N):
    seq = [seqmaker(n) for n in range(st,N+1)]
    sum = [np.sum(seq[1:n+1]) for n in range(1,N)]
    return sum



def seqsumplot(seq = True, st=1, N = 100):
    if seq:
        values = []
        for n in range(st, N + 1):
            x_n = seqmaker(n)
            values.append(x_n)
            # print('Iteration ',n, ' x_n = ', format(x_n,'20.15f'))
    else:
        values = summaker(st, N)
    plt.plot(values, 'ro') # vi skal starte ved st i plottet!!!
    plt.title("$x_n$ som funktion af $n$", size=25)
    plt.xlabel("$n$")
    plt.ylabel("$x_n$")
    plt.grid(True)
    plt.show()

#Overstående er ikke færdig!!!!!!!!!!!!!!!!!!!
seqsumplot(False, 1,10)




