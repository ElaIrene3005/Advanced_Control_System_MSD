import numpy as np
from scipy.linalg import solve_continuous_are
from numpy.linalg import inv

m = 1
b = 20
k = 5

#Matriks state space
A = np.array([[0, 1],
              [-k/m, -b/m]])

B = np.array([[0],
              [1/m]])

#Cost Function LQR
C = np.eye(2)
Q = C.T @ C     # Q = I (meminimalkan posisi dan kecepatan)
R = np.array([[1]])  # Penalti kontrol

#Gain LQR
P = solve_continuous_are(A, B, Q, R) #Persamaan Riccati
K = inv(R) @ B.T @ P
Acl = A - B @ K
print(K)