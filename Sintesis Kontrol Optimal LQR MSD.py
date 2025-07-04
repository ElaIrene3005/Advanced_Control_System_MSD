import control as ctrl
import matplotlib.pyplot as plt
import numpy as np

# Parameter fisik MSD
m = 1.0     
b = 20.0   
k = 5.0    

# Matriks keadaan linear (2 state: posisi dan kecepatan)
A = np.array([[0, 1],
              [-k/m, -b/m]])
B = np.array([[0],
              [1/m]])
C = np.array([[1, 0]])  # hanya posisi sebagai output
D = np.array([[0]])

# Buat sistem state-space
ss = ctrl.ss(A, B, C, D)

# Cek keterkendalian
ctrb = ctrl.ctrb(A, B)
print("Rank controllability matrix:", np.linalg.matrix_rank(ctrb))

# Bobot LQR
Q = np.array([[1000, 0],
              [0, 1]])   # prioritas pada posisi
R = 0.01                # penalti input kecil

# Hitung gain LQR
K, S, E = ctrl.lqr(A, B, Q, R)
print("Gain LQR:", K)

# Sistem baru setelah kontrol optimal
A_new = A - B @ K
ss_new = ctrl.ss(A_new, B, C, D)

# Simulasi
dt = 0.01
Tmax = 10
t = np.arange(0.0, Tmax, dt)
x0 = np.array([1.0, 0.0])  # posisi awal 1m, kecepatan 0

# Input = 0 (karena regulator)
u = np.zeros_like(t)

# Simulasi sistem terkendali
t_out, y_out, x_out = ctrl.forced_response(ss_new, T=t, U=u, X0=x0, return_x=True)

# Plot posisi dan kecepatan
plt.figure(figsize=(10,6))

plt.subplot(2,1,1)
plt.plot(t_out, x_out[0], label='Posisi (m)', color='blue')
plt.ylabel('Posisi')
plt.grid()
plt.legend()

plt.subplot(2,1,2)
plt.plot(t_out, x_out[1], label='Kecepatan (m/s)', color='red')
plt.ylabel('Kecepatan')
plt.xlabel('Waktu (s)')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()