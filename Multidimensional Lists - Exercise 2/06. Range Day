def move(direction, steps):
    row_to_move = (directions[direction][0] * steps) + my_position[0]
    col_to_move = (directions[direction][1] * steps) + my_position[1]

    if not (0 <= row_to_move < SIZE and 0 <= col_to_move < SIZE):
        return my_position
    if matrix[row_to_move][col_to_move] == "x":
        return my_position
    else:
        return [row_to_move, col_to_move]


def shoot(direction):
    r = my_position[0] + directions[direction][0]
    c = my_position[1] + directions[direction][1]

    while 0 <= r < SIZE and 0 <= c < SIZE:
        if matrix[r][c] == "x":
            matrix[r][c] = "."
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


SIZE = 5

matrix = []
my_position = []
total_targets = 0
targets_hit = 0
targets_hit_position = []


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    matrix.append(input().split())

    if "A" in matrix[row]:
        my_position = row, matrix[row].index("A")

    total_targets += matrix[row].count("x")


N = int(input())

for _ in range(N):
    command = input().split()

    if command[0] == "move":
        my_position = move(command[1], int(command[2]))
    elif command[0] == "shoot":
        targets_down_position = shoot(command[1])

        if targets_down_position:
            targets_hit_position.append(targets_down_position)
            targets_hit += 1

        if targets_hit == total_targets:
            print(f"Training completed! All {total_targets} targets hit.")
            break
else:
    print(f"Training not completed! {total_targets - targets_hit} targets left.")
    
print(*targets_hit_position, sep="\n")
