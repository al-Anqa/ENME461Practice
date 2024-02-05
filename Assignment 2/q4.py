from sympy import symbols, solve
import numpy as np

n = symbols('n', real=True) # Natural frequency
w = 85 * 2 * np.pi
z_list = [0.6, 0.8]
const = (1 / 0.98)**2

for z in z_list:
    eq1 = (1 - (w/n)**2)**2 + (2 * z * w / n)**2 - const
    sol = solve(eq1)
    print(sol) # We ignore negative solutions