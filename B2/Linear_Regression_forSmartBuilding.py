import pandas as pd

data = pd.read_csv("data.csv", sep = ";")

height_val = data['ChieuCao'].values; weight_val = data['CanNang'].values; n_val = len(data['Mau'])

total_height = height_val.sum(); print(f'total_height = {total_height}')
total_weight = weight_val.sum(); print(f'total_weight = {total_weight}')
total_height_square = (height_val**2).sum(); print(f'total_height_square = {total_height_square}')
total_weight_and_height = (height_val * weight_val).sum(); print(f'total_weight_height = {total_weight_and_height}')

sigma_1 = ((total_weight_and_height / n_val) - ((total_height / n_val) * (total_weight / n_val))) / ((total_height_square / n_val) - ((total_height / n_val)**2))
sigma_0 = (total_weight / n_val) - (sigma_1 * (total_height / n_val))
print(f'y = {round(sigma_0, 2)} + {round(sigma_1, 2)}x')

new_data = 185; result = sigma_0 + sigma_1 * new_data; print(f'f(new_data) = {round(result, 2)}')