from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
pi=np.pi

fig = plt.figure()
ax = plt.axes(projection="3d")
def z_function(x, y):
	z=6*(np.sin(np.radians(pi*x)))+ (np.cos(np.radians(pi*y)))
	return z
a=100
x = np.linspace(-a, a, 50)
y = np.linspace(-a, a, 50)
X, Y = np.meshgrid(x, y)
Z = z_function(X, Y)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, edgecolor='none')
ax.set_title('surface');
ax.set_xlabel('x_test1')
ax.set_ylabel('x_test2')
ax.set_zlabel('y_test')
plt.show()