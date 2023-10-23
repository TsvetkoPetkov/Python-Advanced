rows = int(input())

matrix = []

primary_diagonal_sum = 0

for row in range(rows):
    inner_line = [int(x) for x in input().split()]
    matrix.append(inner_line)

    primary_diagonal_sum += matrix[row][row]

print(primary_diagonal_sum)
