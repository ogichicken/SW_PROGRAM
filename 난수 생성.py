import random as rd
import matplotlib.pyplot as plt

numpy = []

print(rd.random())

for x in range(1000):
    numpy.append(rd.random() * 3)

plt.plot(numpy)
plt.show()


