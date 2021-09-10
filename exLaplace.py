# import sympy as sym
# from sympy.abc import  s, x, t, a , b

# U = sym.laplace_transform( 1, t, s) 

# U = sym.laplace_transform( sym.exp(-a * t), t, s)

# U = sym.laplace_transform( sym.sin(a * t), t, s)

# U = sym.laplace_transform( sym.sin(a * t) * sym.exp(-b * t), t, s)

#Transformada de Laplace
# Y = (s + 2) /  (s ** 2 + 4 * s + 3)
# y = sym.inverse_laplace_transform(Y, s, t)

# F = sym.apart(Y)

# Propriedades da transformada de Laplace

# import sympy as sym
# from sympy.abc import  s, t, a , b, c

# x1 = sym.sin( a * t)
# x2 = sym.cos( b * t)

# X1 = sym.laplace_transform(x1, t, s)
# X2 = sym.laplace_transform(x2, t, s)

# x3 = c * x1 + x2
# X3 = sym.laplace_transform(x3, t, s)
# X3[0]


# import symbol as sym
# from sympy.abc import s, t, a, b

# t0 = sym.symbols('t0')

# x1 = sym.exp(-a * (t - t0)*sym.Heaviside(t - t0))
# X1 = sym.laplace_transform(x1, t, s)

# X1[0]

import sympy as sym
from sympy.abc import  s, t, a , b, c

w = sym.symbols('w')
x1 = sym.sin( w * t) * sym.exp(- a * t)
X1 = sym.laplace_transform(x1, t, s)
X1[0]
print(X1)
