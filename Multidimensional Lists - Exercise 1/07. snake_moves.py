from collections import deque

rows, cols = [int(x) for x in input().split()]
word = list(input())

copy_word = deque(word)

for row in range(rows):
    while len(copy_word) < cols:
        copy_word.extend(word)

    if row % 2 == 0:
        print(*[copy_word.popleft() for _ in range(cols)], sep="")
    else:
        print(*[copy_word.popleft() for _ in range(cols)][::-1], sep="")
