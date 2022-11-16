import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

x, y, z = sym.symbols('x y z')

prob = (sym.sin(10*(x**2+y**2)))/10

xs= np.arange(-5, 5, 0.1)
ys = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(xs, ys)
zs = [(sym.N(prob.subs({x:X[i],y:Y[i]}))) for i in range]
print(zs)

