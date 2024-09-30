import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers

# Tạo dữ liệu huấn luyện
x_train = np.linspace(0, 1, 100)  # 100 điểm từ 0 đến 1
y_train = np.sin(6 * np.pi * x_train)  # Hàm mục tiêu sin(6x)

# Xây dựng mô hình mạng neuron
model = tf.keras.Sequential([
    layers.Dense(50, activation='relu', input_shape=(1,)),  # Lớp ẩn đầu tiên với 50 neuron, hàm kích hoạt ReLU
    layers.Dense(50, activation='relu'),                    # Lớp ẩn thứ hai với 50 neuron
    layers.Dense(1)                                         # Lớp đầu ra với 1 neuron để dự đoán giá trị hàm f(x)
])

# Compile mô hình
model.compile(optimizer='adam', loss='mse')

# Huấn luyện mô hình
history = model.fit(x_train, y_train, epochs=500, verbose=0)

# Dự đoán kết quả sau khi huấn luyện
y_pred = model.predict(x_train)

# Vẽ kết quả xấp xỉ và hàm thực sự
plt.plot(x_train, y_train, label="f(x) = sin(6x)", color="blue")
plt.plot(x_train, y_pred, label="Neural Network Approximation", color="red", linestyle="--")
plt.legend()
plt.title("Approximation of f(x) = sin(6x) using Neural Network")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
