import numpy as np
import matplotlib.pyplot as plt

a = 1
t = np.linspace(0, np.pi/2, 1000)
x = a * np.sin(t) * np.cos(t)**2
y = a * np.sin(t)**2 * np.cos(t)

plt.figure(figsize=(8, 6))
plt.plot(x, y, color='blue')
plt.title(r'Кривая: $x = a \sin t \cos^2 t$, $y = a \sin^2 t \cos t$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.savefig('curve3.png', dpi=300)
plt.close()

#Задание 5

t = np.linspace(0, 9, 1000)
x = t**2
y = (4/3) * t**(3/2)
z = t

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, color='red')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.savefig('curve5_3d.png', dpi=300)
