rows = int(input())

matrix = []

for _ in range(rows):
    inner_line = [int(x) for x in input().split(", ")]
    matrix.extend(inner_line)

print(matrix)
