import matplotlib.pyplot as plt


x = [x for x in range(1,12)]
y = [29, 45, 60, 73, 86, 99, 111, 123, 135, 147, 154]
plt.plot(x, y, 'ro')
plt.title("$\ell$ som funktion af $x$", size = 25)
plt.xlabel("$x$")
plt.ylabel("$\ell$")
plt.grid(True)
plt.show()

x = [x for x in range(1,13)]
y = [29, 45, 60, 73, 86, 99, 111, 123, 135, 147, 159, 170]
plt.plot(x, y, 'ro')
plt.title("$\ell$ som funktion af $x$. Dårlig fiks.", size = 25)
plt.xlabel("$x$")
plt.ylabel("$\ell$")
plt.grid(True)
plt.show()






