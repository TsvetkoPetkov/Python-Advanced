from collections import deque

names = deque()

while True:
    name = input()

    if name == "Paid":
        while names:
            print(names.popleft())
        continue

    if name == "End":
        break

    names.append(name)

print(f"{len(names)} people remaining.")
