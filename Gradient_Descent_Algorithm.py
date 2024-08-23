# Gradient Descent Algorithm for a simple function f(x) = x^2 - 2x + 2
def f(x):
    return x**2 - 2*x + 2

def f_prime(x):
    return 2*x - 2

x = 3
learning_rate = 0.3
num_iterations = 10

for i in range(num_iterations):
    gradient = f_prime(x)
    x = x - learning_rate * gradient
    print(f'Iteration {i+1}: x = {x}, f(x) = {f(x)}')
