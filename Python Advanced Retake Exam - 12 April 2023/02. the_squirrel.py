from collections import deque

size = int(input())
where_to_move = deque(input().split(", "))

matrix = []
squirrel_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    matrix.append(input())

    if "s" in matrix[row]:
        squirrel_pos = [row, matrix[row].index("s")]

hazelnuts_counter = 0

while hazelnuts_counter < 3:
    command = where_to_move[0]

    r = directions[command][0] + squirrel_pos[0]
    c = directions[command][1] + squirrel_pos[1]

    if 0 <= r < size and 0 <= c < size:
        if matrix[r][c] == "h":
            hazelnuts_counter += 1
        elif matrix[r][c] == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            break
    else:
        print("The squirrel is out of the field.")
        break

    squirrel_pos = [r, c]
    where_to_move.popleft()
else:
    if hazelnuts_counter == 3:
        print("Good job! You have collected all hazelnuts!")
    else:
        print("There are more hazelnuts to collect.")


print(f"Hazelnuts collected: {hazelnuts_counter}")
