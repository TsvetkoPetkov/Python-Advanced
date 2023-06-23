def check_valid(rows, cols, indices):
    if len(indices) == 4:
        row1, col1, row2, col2 = indices
    else:
        return

    if rows > row1 and rows > row2 and cols > col1 and cols > col2 and len(indices) == 4:
        if row1 >= 0 and row2 >= 0 and col1 >= 0 and col2 >= 0:
            return True
    else:
        return False


def swap_command(command, indices):
    if check_valid(rows, cols, indices) and command == "swap":
        row1, col1, row2, col2 = indices

        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        print(*[" ".join(r) for r in matrix], sep='\n')
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

while True:
    command, *indices = [int(x) if x.isdigit() else x for x in input().split()]

    if command == "END":
        break

    swap_command(command, indices)
