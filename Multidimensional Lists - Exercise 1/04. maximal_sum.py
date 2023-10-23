rows, cols = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    inner_line = [int(x) for x in input().split()]
    matrix.append(inner_line)

max_sum = -1000

numbers = []

for row in range(rows - 2):
    curr_sum = 0
    for col in range(cols - 2):
        row_one_first = matrix[row][col]
        row_one_second = matrix[row][col + 1]
        row_one_third = matrix[row][col + 2]

        row_two_first = matrix[row + 1][col]
        row_two_second = matrix[row + 1][col + 1]
        row_two_third = matrix[row + 1][col + 2]

        row_three_first = matrix[row + 2][col]
        row_three_second = matrix[row + 2][col + 1]
        row_three_third = matrix[row + 2][col + 2]

        curr_sum = row_one_first + row_one_second + row_one_third + row_two_first + row_two_second + row_two_third + \
                   row_three_first + row_three_second + row_three_third

        if curr_sum > max_sum:
            max_sum = curr_sum
            numbers = [[row_one_first, row_one_second, row_one_third], [row_two_first, row_two_second, row_two_third],
                       [row_three_first, row_three_second, row_three_third]]

print(f"Sum = {max_sum}")
print(*numbers[0])
print(*numbers[1])
print(*numbers[2])
