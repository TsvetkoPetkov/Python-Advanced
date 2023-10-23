rows, cols = [int(x) for x in input().split(", ")]

matrix = []

total_sum = 0

for _ in range(rows):
    inner_line = [int(el) for el in input().split(", ")]
    total_sum += sum(inner_line)
    matrix.append(inner_line)

print(total_sum)
print(matrix)
