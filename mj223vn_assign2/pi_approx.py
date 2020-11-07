import math as m
import random

def pi_error(pi_approx):
    return abs(m.pi - pi_approx)

def calculate_pi(N):
    in_circle = 0
    for i in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if m.pow(x, 2) + m.pow(y, 2) <= 1.0:
            in_circle += 1
            
    pi = 4 * in_circle / N
    return pi


N = 100
for i in range(3):
    pi_approx = calculate_pi(N)
    error = pi_error(pi_approx)
    print(f"The approximated value of pi with {N} number of iterations is: {pi_approx}\n"
            + f"Thats an error from actual pi with {error}\n")
    N = N * 100



