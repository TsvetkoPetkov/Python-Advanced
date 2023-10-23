rows = int(input())

matrix = []

cols = 0

for _ in range(rows):
    text = list(input())
    matrix.append(text)
    cols = len(text)

searched_symbol = input()

coordinates = []

done = False

for row in range(rows):
    if done:
        break
    for col in range(cols):
        if matrix[row][col] == searched_symbol:
            coordinates.append(row)
            coordinates.append(col)
            done = True
            break

if done:
    print(tuple(coordinates))
else:
    print(f"{searched_symbol} does not occur in the matrix")
