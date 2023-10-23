numbers = [float(x) for x in input().split()]
one_time_numbers = []

for num in numbers:
    if num not in one_time_numbers:
        one_time_numbers.append(num)

for num in one_time_numbers:
    print(f"{num:.1f} - {numbers.count(num)} times")
