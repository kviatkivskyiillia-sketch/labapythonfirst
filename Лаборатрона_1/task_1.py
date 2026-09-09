import math

m = float(input("Enter m: "))

if m > -2:
    z = 1 / math.sqrt(m + 2)
    print(f'z = {z}')
else:
    print('Помилка: m має бути більше ніж -2')