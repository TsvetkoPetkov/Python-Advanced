rows = int(input())

matrix = []

for _ in range(rows):
    inner_line = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix.append(inner_line)

print(matrix)
