import numpy as np

def fx(x):
    return x**2 + 6*np.sin(x)

def f_prime(x):
    return 2*x + 6*np.cos(x)

x = 0
learning_rate = 0.001
num_iterations = 1000000
epsilon = 1e-3

for i in range(num_iterations):
    gradient = f_prime(x)
    if abs(gradient) <= epsilon:
        print(f'Stopping early at iteration {i+1}: |f\'(x)| = {abs(gradient)} ≤ {epsilon}')
        break
    x = x - learning_rate * gradient
    print(f'Iteration {i+1}: x = {x}, f(x) = {fx(x)}')
