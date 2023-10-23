from collections import deque

boxes = [int(x) for x in input().split()]
capacity = int(input())
first_capacity = capacity

counter = 1

for box in boxes.copy():
    last_box = boxes.pop()

    if last_box <= first_capacity:
        first_capacity -= last_box
    else:
        counter += 1
        first_capacity = capacity - last_box


print(counter)
