from collections import deque

bees = deque([int(x) for x in input().split()])
nectar_values = deque([int(x) for x in input().split()])
symbols = deque(x for x in input().split())

total_honey = []

while bees and nectar_values:
    bee = bees.popleft()
    nectar = nectar_values.pop()

    if nectar < bee:
        bees.appendleft(bee)
    elif nectar >= bee:
        symbol = symbols.popleft()
        if symbol == '+':
            honey_made = bee + nectar
            total_honey.append(honey_made)
        elif symbol == '-':
            total_honey.append(abs(bee - nectar))
        elif symbol == '*':
            total_honey.append(bee * nectar)
        elif symbol == '/':
            if nectar == 0:
                continue
            else:
                total_honey.append(bee / nectar)

print(f"Total honey made: {sum(total_honey)}")

if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
elif nectar_values:
    print(f"Nectar left: {', '.join([str(x) for x in nectar_values])}")
