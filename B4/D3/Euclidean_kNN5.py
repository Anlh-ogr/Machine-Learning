import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

new_sample = np.array([[21, 52]])

training_data = np.array([[22, 50], [24, 45], [23, 47], [21, 49], [25, 44], [19, 55], [20, 60],
                          [18, 58], [17, 57], [20, 62], [23, 46], [24, 48], [19, 54], [18, 56]])

training_labels = np.array(["LR", "BR", "LR", "LR", "BR", "LR", "BR", "BR", "BR", "BR", "LR", "LR", "LR", "BR"])
label_mapping = {"LR": 0, "BR": 1}
numerical_labels = np.array([label_mapping[label] for label in training_labels])

knn_classifier = KNeighborsClassifier(n_neighbors=5)
knn_classifier.fit(training_data, numerical_labels)

predicted_label = knn_classifier.predict(new_sample)
predicted_room_type = 'Living Room' if predicted_label[0] == 0 else 'Bedroom'

plt.figure(figsize=(10, 6))
plt.scatter(training_data[numerical_labels == 0][:, 0], training_data[numerical_labels == 0][:, 1], color='red', marker='s', label='Living Room')
plt.scatter(training_data[numerical_labels == 1][:, 0], training_data[numerical_labels == 1][:, 1], color='blue', marker='o', label='Bedroom')

marker = 'o' if predicted_label[0] == 1 else 's'
plt.scatter(new_sample[:, 0], new_sample[:, 1], color='green', marker=marker, s=100, label=f'New Sample ({predicted_room_type})')

print(f'The room type of the new sample (21°C, 52%) is: {predicted_room_type}')

plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.title('k-NN Classification Result')
plt.legend()
plt.grid(True)
plt.show()