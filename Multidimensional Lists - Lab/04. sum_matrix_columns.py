rows, cols = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    inner_line = [int(x) for x in input().split()]
    matrix.append(inner_line)

for col in range(cols):
    curr_sum = 0
    for row in range(rows):
        curr_sum += matrix[row][col]

    print(curr_sum)
