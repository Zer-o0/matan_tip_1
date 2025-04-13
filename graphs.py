import numpy as np
import matplotlib.pyplot as plt
#Задание 3
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
plt.savefig('3.png', dpi=300)
plt.close()
#Задание 4
a = 1
theta = np.linspace(0, 2*np.pi, 1000)
cos_theta = np.cos(theta)
sin_theta = np.sin(theta)


numerator = a**2 * cos_theta**3 * sin_theta
denominator = cos_theta**6 + sin_theta**6
r = numerator / (denominator + 1e-12)  # Защита от деления на ноль


plt.figure(figsize=(8, 8))
plt.polar(theta, r, color='green')
plt.title(r'Кривая: $x^6 + y^6 = a^2 x^3 y$') 
plt.grid(True)
plt.savefig('4.png', dpi=300)
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
plt.savefig('5.png', dpi=300)

