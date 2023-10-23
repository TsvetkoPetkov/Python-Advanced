import math
from collections import deque

expression = deque([x for x in input().split()])

numbers = []

while expression:
    char = expression.popleft()

    if char.isnumeric() or char.replace('-', '').isnumeric():
        numbers.append(int(char))
    elif char == '*':
        result = numbers[0]
        for n in range(1, len(numbers)):
            result *= numbers[n]
        numbers.clear()
        numbers.append(result)
    elif char == '/':
        result = numbers[0]
        for n in range(1, len(numbers)):
            result /= numbers[n]
        numbers.clear()
        numbers.append(math.floor(result))
    elif char == '+':
        result = numbers[0]
        for n in range(1, len(numbers)):
            result += numbers[n]
        numbers.clear()
        numbers.append(result)
    elif char == '-':
        result = numbers[0]

        for n in range(1, len(numbers)):
            result -= numbers[n]
        numbers.clear()
        numbers.append(result)

print(*numbers)
