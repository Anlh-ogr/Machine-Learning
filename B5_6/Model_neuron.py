from tensorflow import keras
from tensorflow.keras.layers import Dropout, Input
from tensorflow.keras.datasets import mnist

# Load the MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Normalize the data
X_train = X_train / 255.0
X_test = X_test / 255.0

# Build the new model
model_new = keras.models.Sequential([
    Input(shape=[28, 28]),  # Use Input layer to specify the input shape
    keras.layers.Flatten(),  # Flatten the input
    keras.layers.Dense(512, activation="relu"),  # Increase the number of neurons to 512
    Dropout(0.2),  # Add Dropout to prevent overfitting
    keras.layers.Dense(256, activation="relu"),  # Add a hidden layer with 256 neurons
    Dropout(0.2),
    keras.layers.Dense(128, activation="relu"),  # Add a hidden layer with 128 neurons
    keras.layers.Dense(10, activation="softmax")  # Output layer with 10 neurons
])

# Compile the model
model_new.compile(loss="sparse_categorical_crossentropy",
                  optimizer="adam",  # Use Adam optimizer
                  metrics=["accuracy"])

# Train the model
history_new = model_new.fit(X_train, y_train, epochs=30, validation_data=(X_test, y_test))

# Evaluate the new model
test_loss_new, test_acc_new = model_new.evaluate(X_test, y_test)
print(f"Test accuracy with new model: {test_acc_new}")