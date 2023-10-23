rows, cols = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    inner_line = [char for char in input().split()]
    matrix.append(inner_line)

counter = 0

for row in range(rows-1):
    for col in range(cols-1):
        curr_el = matrix[row][col]
        under_el = matrix[row+1][col]
        next_el = matrix[row][col+1]
        diagonal = matrix[row+1][col+1]

        if curr_el == under_el and curr_el == next_el and curr_el == diagonal:
            counter += 1
print(counter)
