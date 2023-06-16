from collections import deque

time = deque([int(x) for x in input().split()])
tasks = deque([int(x) for x in input().split()])

darth_vader_ducky_counter = 0
thor_ducky_counter = 0
big_blue_rubber_ducky_counter = 0
small_yellow_rubber_ducky = 0

while time and tasks:
    first_time = time[0]
    last_task = tasks[-1]

    current_time = first_time * last_task

    if 0 <= current_time <= 60:
        darth_vader_ducky_counter += 1
        time.popleft()
        tasks.pop()
    elif 61 <= current_time <= 120:
        thor_ducky_counter += 1
        time.popleft()
        tasks.pop()
    elif 121 <= current_time <= 180:
        big_blue_rubber_ducky_counter += 1
        time.popleft()
        tasks.pop()
    elif 181 <= current_time <= 240:
        small_yellow_rubber_ducky += 1
        time.popleft()
        tasks.pop()
    elif current_time > 240:
        tasks.pop()
        tasks.append(last_task-2)
        time.popleft()
        time.append(first_time)


print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {darth_vader_ducky_counter}")
print(f"Thor Ducky: {thor_ducky_counter}")
print(f"Big Blue Rubber Ducky: {big_blue_rubber_ducky_counter}")
print(f"Small Yellow Rubber Ducky: {small_yellow_rubber_ducky}")
