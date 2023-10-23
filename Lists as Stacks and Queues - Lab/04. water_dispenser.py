from collections import deque

quantity = int(input())
people = deque()

while True:
    name = input()

    if name == "Start":
        break

    people.append(name)

while True:
    command = input()

    if command == "End":
        break

    splitted_command = command.split()

    if splitted_command[0].isdigit():
        liters = int(splitted_command[0])

        if quantity >= liters:
            print(f"{people.popleft()} got water")
            quantity -= liters
        else:
            print(f"{people.popleft()} must wait")
    elif splitted_command[0] == "refill":
        amount_to_refill = int(splitted_command[1])
        quantity += amount_to_refill

print(f"{quantity} liters left")
