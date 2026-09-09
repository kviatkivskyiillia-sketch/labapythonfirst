n = int(input("Напишіть кількість днів: "))

distance = 10.0
total = 0.0
day = 1

while day <= n:
    total += distance
    distance *= 1.10
    day += 1

print(f"За = {n} днів він пробіжить: {total} км ")