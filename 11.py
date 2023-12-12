import matplotlib.pyplot as plt

x = [x for x in range(-10, 10)]
y = [2*t for t in x]
plt.plot(x, y, marker='o')

plt.axis([-20, 20, -20, 20])
plt.show()


# LAB 11-2
import math
import matplotlib.pyplot as plt

x = []
y = []

for angle in range(360):
    x.append(angle)
    y.append(math.sin(math.radians(angle)))

plt.plot(x, y)
plt.title("SINE WAVE")
plt.show()
