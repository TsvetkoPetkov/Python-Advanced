from collections import deque

N = int(input())

pumps_info = deque([[int(x) for x in input().split()] for pump in range(N)])

tank = 0

pumps_info_copy = pumps_info.copy()
index = 0

while pumps_info_copy:
    amount, km_to_next = pumps_info_copy.popleft()

    tank += amount

    if tank >= km_to_next:
        tank -= km_to_next
    else:
        pumps_info.rotate(-1)
        pumps_info_copy = pumps_info.copy()
        index += 1
        tank = 0

print(index)
