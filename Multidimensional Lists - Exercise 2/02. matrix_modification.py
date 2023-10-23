rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

def check_valid(indices):
    row, col, value = indices

    if row >= 0 and row <= rows - 1 and col >= 0 and col <= rows - 1:
        return True
    else:
        print("Invalid coordinates")
        return False


def matrix_modification(command, indices):
    if check_valid(indices):
        row, col, value = indices
        if command == "Add":
            matrix[row][col] += value
        elif command == "Subtract":
            matrix[row][col] -= value
        return matrix


while True:
    command, *indices = [int(x) if x.lstrip('-+').isdigit() else x for x in input().split()]

    if command == "END":
        break

    matrix_modification(command, indices)

for row in matrix:
    res = ''
    for num in row:
        res += str(num) + " "
    print(res[:-1])
