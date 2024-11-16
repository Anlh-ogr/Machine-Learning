# data
'''                 M = 1; N = 12
        model           weight(kg)              height(m)
        1               30                      70
        2               40                      90
        3               40                      100
        4               50                      120
        5               50                      130
        6               50                      150
        7               60                      160
        8               70                      190
        9               70                      200
        10              80                      200
        11              80                      220
        12              80                      230
        ...
        ...

        x               35                      ?               '''

# create variable and arrays for save the data
M_val = 1
N_val = 12
x_val = 35

weight = [30, 40, 40, 50, 50, 50, 60, 70, 70, 80, 80, 80]
height = [70, 90, 100, 120, 130, 150, 160, 190, 200, 200, 220, 230]

x = weight
y = height

# other variables needed
sum_x = sum(x);  print(f'sum_x = {sum_x}')
sum_y = sum(y);  print(f'sum_y = {sum_y}')
sum_x2 = sum([i**2 for i in x]);  print(f'sum_x2 = {sum_x2}')
sum_x_div_N_2 = (sum_x/N_val)**2;  print(f'sum_x_div_N_2 = {round(sum_x_div_N_2, 2)}')
sum_xy = sum([x[i]*y[i] for i in range(N_val)]);  print(f'sum_xy = {sum_xy}')

# total_1
numerator_a = (sum_xy / N_val) - ((sum_x / N_val) * (sum_y / N_val))
denominator_a = (sum_x2 / N_val) - (sum_x / N_val)**2
total_1 = numerator_a / denominator_a;  print(f'total_1 = {round(total_1, 2)}')

# total_0
total_0 = (sum_y / N_val) - (total_1 * (sum_x / N_val));  print(f'total_0 = {round(total_0, 2)}')

# f(x)
print(f'f(x) = y = total_0 + total_1x = {round(total_0, 2)} + {round(total_1, 2)}x')

new_data = 35
result = total_0 + total_1 * new_data;  print(f'f({new_data}) = {round(result, 2)}')