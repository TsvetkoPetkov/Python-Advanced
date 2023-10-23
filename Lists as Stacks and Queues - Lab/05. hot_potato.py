from collections import deque

kids_names = deque(input().split())

toss = int(input())

finish = ""
while len(kids_names) > 1:
    kids_names.rotate(-toss)
    finished = kids_names.pop()
    print(f"Removed {finished}")

print(f"Last is {kids_names.pop()}")
