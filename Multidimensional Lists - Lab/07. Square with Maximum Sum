rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    inner_line = [int(x) for x in input().split(", ")]
    matrix.append(inner_line)

max_sum = - 10000

nums_to_print = []

for row in range(rows-1):
    curr_sum = 0
    numbers = []
    for col in range(cols-1):
        curr_el = matrix[row][col]
        el_under = matrix[row+1][col]
        next_el = matrix[row][col+1]
        diagonal = matrix[row+1][col+1]

        curr_sum = curr_el + el_under + next_el + diagonal

        if curr_sum > max_sum:
            max_sum = curr_sum
            numbers = [[curr_el, next_el], [el_under, diagonal]]
            nums_to_print = numbers

print(*nums_to_print[0])
print(*nums_to_print[1])
print(max_sum)
