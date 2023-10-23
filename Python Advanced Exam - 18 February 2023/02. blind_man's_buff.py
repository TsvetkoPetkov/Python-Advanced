N, M = [int(x) for x in input().split()]

playground = []
my_pos = []

for row in range(N):
    playground.append(input().split())

    if "B" in playground[row]:
        my_pos = [row, playground[row].index("B")]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

touched_opponents = 0
moves_made = 0

while True:
    command = input()

    if command == "Finish":
        break

    r = my_pos[0] + directions[command][0]
    c = my_pos[1] + directions[command][1]

    if not (0 <= r < N and 0 <= c < M):
        continue

    if playground[r][c] == "P":
        touched_opponents += 1
        playground[r][c] = "-"
    elif playground[r][c] == "O":
        continue

    my_pos = [r, c]
    moves_made += 1

    if touched_opponents == 3:
        break

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")
