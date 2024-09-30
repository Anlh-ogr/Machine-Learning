import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers #type: ignore

x_train = np.linspace(0, 1, 100)
y_train = np.sin(6 * np.pi * x_train)

model = tf.keras.Sequential([
    layers.Dense(50, activation='relu', input_shape=(1,)),
    layers.Dense(50, activation='relu'),
    layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse')
history = model.fit(x_train, y_train, epochs=500, verbose=0)
y_pred = model.predict(x_train)

plt.plot(x_train, y_train, label="f(x) = sin(6x)", color="blue")
plt.plot(x_train, y_pred, label="Neural Network Approximation", color="red", linestyle="--")
plt.legend()
plt.title("Approximation of f(x) = sin(6x) using Neural Network")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
