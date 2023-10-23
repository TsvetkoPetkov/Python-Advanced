SIZE = int(input())

matrix = []

alice_position = []
rabbit_position = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

collected_tea = 0

for row in range(SIZE):
    matrix.append(input().split())

    if "A" in matrix[row]:
        alice_position = [row, matrix[row].index("A")]
        matrix[row][alice_position[1]] = "*"

    if "R" in matrix[row]:
        rabbit_position = [row, matrix[row].index("R")]

while collected_tea < 10:
    current_direction = input()

    row = alice_position[0] + directions[current_direction][0]
    col = alice_position[1] + directions[current_direction][1]

    if not (0 <= row < SIZE and 0 <= col < SIZE):
        break
    if [row, col] == rabbit_position:
        matrix[row][col] = "*"
        break

    if matrix[row][col].isnumeric():
        collected_tea += int(matrix[row][col])
        matrix[row][col] = "*"

    if matrix[row][col] == ".":
        matrix[row][col] = "*"

    alice_position = [row, col]

if collected_tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

print(*[" ".join(row) for row in matrix], sep="\n")
