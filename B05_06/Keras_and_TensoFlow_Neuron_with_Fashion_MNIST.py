import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras
from tensorflow.keras.layers import Dropout, Input  # type: ignore

# Load the Fashion MNIST dataset
mnist_fashion = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = mnist_fashion.load_data()

# Normalize the data
data_train, data_valid = train_images[5000:] / 255.0, train_images[:5000] / 255.0
labels_train, labels_valid = train_labels[5000:], train_labels[:5000]
data_test = test_images / 255.0

# Build the model
model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    Dropout(0.2),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(data_train, labels_train, epochs=5, validation_data=(data_valid, labels_valid))

# Evaluate the model
test_loss, test_acc = model.evaluate(data_test, test_labels)
print(f"The model's accuracy is {test_acc}")

# Plot the training history
plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.legend()
plt.show()
