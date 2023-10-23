size = int(input())

battlefield = []
submarine_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    battlefield.append(list(input()))

    if "S" in battlefield[row]:
        submarine_pos = [row, battlefield[row].index("S")]
        battlefield[submarine_pos[0]][submarine_pos[1]] = "-"

cruisers = 3
mines_hit = 0

while True:
    command = input()

    r = submarine_pos[0] + directions[command][0]
    c = submarine_pos[1] + directions[command][1]

    if 0 <= r < size and 0 <= c < size:
        if battlefield[r][c] == "*":
            battlefield[r][c] = '-'
            mines_hit += 1
            if mines_hit == 3:
                print(f"Mission failed, U-9 disappeared! Last known coordinates [{r}, {c}]!")
                submarine_pos = [r, c]
                break
        elif battlefield[r][c] == "C":
            cruisers -= 1
            battlefield[r][c] = "-"

            if cruisers == 0:
                print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
                submarine_pos = [r, c]
                break

        submarine_pos = [r, c]

battlefield[submarine_pos[0]][submarine_pos[1]] = "S"

print(*["".join(x) for x in battlefield], sep="\n")
