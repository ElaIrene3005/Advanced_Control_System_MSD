import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parameter sistem
m = 1     # massa (kg)
b = 20    # redaman (Ns/m)
k = 5     # pegas (N/m)

# Sistem tanpa kontrol (gaya kontrol u = 0)
def msd_without_control(x, t):
    x1, x2 = x
    dx1dt = x2
    dx2dt = -(k/m)*x1 - (b/m)*x2
    return [dx1dt, dx2dt]

# Waktu dan kondisi awal
t = np.linspace(0, 10, 1000)
x0 = [1, 0]  # posisi awal 1 m, kecepatan awal 0

# Simulasi tanpa kontrol
x_free = odeint(msd_without_control, x0, t)

# Plot
plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.plot(t, x_free[:,0], label='Posisi (tanpa kontrol)', color='blue')
plt.ylabel('Posisi (m)')
plt.grid()

plt.subplot(2,1,2)
plt.plot(t, x_free[:,1], label='Kecepatan (tanpa kontrol)', color='red')
plt.ylabel('Kecepatan (m/s)')
plt.xlabel('Waktu (s)')
plt.grid()
plt.tight_layout()
plt.show()