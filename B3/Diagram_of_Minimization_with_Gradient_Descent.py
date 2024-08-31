import numpy as np
import matplotlib.pyplot as plt

def fx_Function(x):
    return x**2 + 6*np.sin(x)

x_val = np.linspace(-4, 4, 1000)
y_val = fx_Function(x_val)

plt.plot(x_val, y_val, label='f(x) = x^2 + 6sin(x)')
plt.title('f(x) = x^2 + 6sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()

