import sympy as sym
from sympy import exp
from sympy.abc import x

integrate = sym.integrate(((x + 1) * exp(x)), x)
print('Первообразная подынтегральной функции - ', integrate)
