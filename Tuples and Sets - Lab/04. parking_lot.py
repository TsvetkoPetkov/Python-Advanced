n = int(input())

cars_set = set()

for _ in range(n):
    command, number = input().split(', ')

    if command == "IN":
        cars_set.add(number)
    elif command == "OUT":
        if number in cars_set:
            cars_set.remove(number)

if len(cars_set) > 0:
    print(*cars_set, sep="\n")
else:
    print("Parking Lot is Empty")
