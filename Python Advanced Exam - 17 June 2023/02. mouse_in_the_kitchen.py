N, M = [int(x) for x in input().split(",")]

matrix = []
mouse_position = []
cheese_counter = 0

for row in range(N):
    matrix.append(list(input()))

    if "M" in matrix[row]:
        mouse_position = [row, matrix[row].index("M")]
        matrix[mouse_position[0]][mouse_position[1]] = "*"

    if "C" in matrix[row]:
        cheese_counter += matrix[row].count("C")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input()

    if command == "danger":
        print("Mouse will come back later!")
        break

    r = mouse_position[0] + directions[command][0]
    c = mouse_position[1] + directions[command][1]

    if 0 <= r < N and 0 <= c < M:
        if matrix[r][c] == "C":
            cheese_counter -= 1
            matrix[r][c] = "*"
            if cheese_counter == 0:
                mouse_position = [r, c]
                print("Happy mouse! All the cheese is eaten, good night!")
                break
        elif matrix[r][c] == "@":
            continue
        elif matrix[r][c] == "T":
            matrix[r][c] = "*"
            print("Mouse is trapped!")
            mouse_position = [r, c]
            break
        mouse_position = [r, c]
    else:
        print("No more cheese for tonight!")
        break

matrix[mouse_position[0]][mouse_position[1]] = "M"

print(*["".join(x) for x in matrix], sep="\n")
