from sympy import symbols, solve
import numpy as np

n = symbols('n', real=True) # Natural frequency
w = 170 * np.pi
z = 0.8

eq1 = (1 - (w/n)**2)**2 + (2 * z * w / n)**2 - 1.04

sol = solve(eq1)
print(sol)