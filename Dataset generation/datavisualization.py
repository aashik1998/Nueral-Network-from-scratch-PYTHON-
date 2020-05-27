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
ax.set_title('z=6sin(pix1)+cos(pix2)');
ax.set_xlabel('X1  (x_test1)')
ax.set_ylabel('X2  (x_test2)')
ax.set_zlabel('Z   (y_test)')
plt.show()