size = int(input())
racing_number = input()

matrix = []
car_coordinates = [0, 0]

tunnel_coordinates = []
km_passed = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    matrix.append(input().split())

    if "T" in matrix[row]:
        tunnel_coordinates.append([row, matrix[row].index("T")])

while True:
    command = input()

    if command == "End":
        print(f"Racing car {racing_number} DNF.")
        break

    r = car_coordinates[0] + directions[command][0]
    c = car_coordinates[1] + directions[command][1]

    if 0 <= r < size and 0 <= c < size:
        if matrix[r][c] == "F":
            matrix[r][c] = "."
            km_passed += 10
            car_coordinates = [r, c]
            print(f"Racing car {racing_number} finished the stage!")
            break
        elif matrix[r][c] == ".":
            km_passed += 10
            car_coordinates = [r, c]
        elif matrix[r][c] == "T":
            matrix[r][c] = "."
            km_passed += 30
            car_coordinates = tunnel_coordinates[1]
            matrix[car_coordinates[0]][car_coordinates[1]] = "."

matrix[car_coordinates[0]][car_coordinates[1]] = "C"

print(f"Distance covered {km_passed} km.")
print(*["".join(x) for x in matrix], sep="\n")
