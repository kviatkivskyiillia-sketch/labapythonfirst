def positive_numbers():
    numbers = [-5, -3, 0, 2, 8, -1, 4]

    positive_numbers = [x for x in numbers if x >= 0]

    if positive_numbers:
        min_positive = min(positive_numbers)
        print(min_positive)
    else:
        print(numbers)

positive_numbers()

def average():

    numbers = [-5, -3, 0, 2, 8, -1, 4]

    suma = 0
    count = 0

    for x in numbers:
        if x > 0:
            suma += x
            count += 1

    average = suma / count
    print(average)

average()

def not_zero():
    numbers = [1, 0, 5, 3, 0, 9, 0, 2]

    result = [x for x in numbers if x != 0][::-1]

    print(*result)

not_zero()