# Biblotek för matematik & grafer
import numpy as np
from matplotlib import pyplot as plt

# Variabler
c = 0.5
A = 0.00195
Densitet = 1.2
m = 0.0138
Vy = 4.53
Vx = 4.53
Vx2 = 4.53
x = 0
y = 0.275
h = 0.0001
k = 0.5 * A * c * Densitet
t = 0
end = 0

# FYSIK 2

# Funktion y av x
def y_fysik2(x_fysik2):
  return x_fysik2 - 4.91 * (x_fysik2/Vx2) ** 2 + 0.275

# Plotta fysik 2
plt.title("Fysik 2 modell")
plt.ylim(0, 2)
x_fysik2 = np.linspace(0, 5, 200)
plt.plot(x_fysik2, y_fysik2(x_fysik2), color="blue", linewidth=7)
plt.ylabel("Höjd [m]")
plt.xlabel("Avstånd [m]")
plt.show()

# RUNGE-KUTTA

# x & y listor
xlist = list()
ylist = list()

# Funktioner för x & y positioner
def Fx(Vx, t):
  return -k/m * Vx ** 2

def Fy(Vy, t):
  return -9.82 -k/m * Vy ** 2

# Runge-kutta lösning
while y > end:
  Kx1 = Fx(Vx, t)
  x1 = Vx + Kx1 * h/2
  Kx2 = Fx(x1, t+h/2)
  x2 = Vx + Kx2 * h/2
  Kx3 = Fx(x2, t+h/2)
  x3 = Vx + Kx3 * h
  Kx4 = Fx(x3, t+h)

  Ky1 = Fy(Vy, t)
  y1 = Vy + Ky1 * h/2
  Ky2 = Fy(y1, t+h/2)
  y2 = Vy + Ky2 * h/2
  Ky3 = Fy(y2, t+h/2)
  y3 = Vy + Ky3 * h
  Ky4 = Fy(y3, t+h)

  t = t + h

  Vx += h*(Kx1+2*Kx2+2*Kx3+Kx4)/6
  Vy += h*(Ky1+2*Ky2+2*Ky3+Ky4)/6

  x += Vx * h
  y += Vy * h

  xlist.append(x)
  ylist.append(y)

# Plotta Runge-kutta
plt.title("Runge-kutta modell")
plt.scatter(xlist, ylist, color="red", )
x = np.linspace(0, 7, 200)
plt.ylim(0, 2)
plt.ylabel("Höjd [m]")
plt.xlabel("Avstånd [m]")
plt.show()
