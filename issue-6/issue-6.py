import sympy

X0 = 0.0
a = 5
x = sympy.Symbol('x')

f = (x / 2) * sympy.sqrt(a ** 2 - x ** 2) + (a ** 2 / 2) * sympy.asin(x / 2)


def calculate_derivatives():
    f1 = sympy.diff(f, x)
    print('Первая производная - ', f1)
    print("f(1) =", f1.subs(x, X0))

    f2 = sympy.diff(f1, x)
    print('Вторая производная - ', f2)
    print("f(2) =", f2.subs(x, X0))


calculate_derivatives()
