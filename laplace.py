import numpy as np
import matplotlib.pyplot as plt


a = 3   # 0 < x < a
b = 3   # 0 < y < b

#Gitter
x_n = 100 #Antall gitterpunkt x-akse
y_n = 100  #Antall gitterpunkt y-akse
x = np.linspace(0, a, x_n)
y = np.linspace(0, b, y_n)
X, Y = np.meshgrid(x, y)

#Initialiserer matrise med grenseverdier
u = np.zeros((x_n, y_n))
u[:, 0] = np.sin(x+1)  #u(x, 0)
u[0, :] = np.sin(y-1)  #u(0, y)
u[:, -1] = 1 #u(x, b)
u[-1, :] = 1 #u(a, y)

it_max = 100

for it in range(0, it_max):
    gammel_u = u.copy()
    for i in range(1, x_n - 1):
        for j in range(1, y_n - 1):
            u[i][j] =  0.25 * (u[i+1][j] + u[i-1][j] + u[i][j+1] + u[i][j-1])
                     
#Plotting    
fig = plt.figure(figsize = (8, 6))
ax = fig.add_subplot(111, projection = '3d')
ax.plot_surface(X, Y, u, cmap = 'viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()