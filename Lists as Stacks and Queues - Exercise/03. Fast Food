from collections import deque

quantity_of_food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

orders_copy = orders.copy()

for order in orders_copy:
    if order <= quantity_of_food:
        orders.popleft()
        quantity_of_food -= order
    else:
        break

if len(orders) == 0:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")
