field_size = int(input())

matrix = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

bunny_position = []
max_eggs = 0
best_direction = ''
best_path = []

for row in range(field_size):
    matrix.append(input().split())

    if "B" in matrix[row]:
        bunny_position = [row, matrix[row].index("B")]

for direction, pos in directions.items():
    row, col = [bunny_position[0] + pos[0], bunny_position[1] + pos[1]]
    current_path = []

    eggs_sum = 0

    while 0 <= row < field_size and 0 <= col < field_size:
        if matrix[row][col] == "X":
            break

        eggs_sum += int(matrix[row][col])
        current_path.append([row, col])

        row += pos[0]
        col += pos[1]

    if eggs_sum >= max_eggs:
        max_eggs = eggs_sum
        best_direction = direction
        best_path = current_path

print(best_direction)
print(*best_path, sep="\n")
print(max_eggs)
