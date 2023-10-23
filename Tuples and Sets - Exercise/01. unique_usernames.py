n = int(input())

unique_names = []

for i in range(n):
    name = input()
    unique_names.append(name)

set_names = set(unique_names)

for _ in set_names:
    print(_)
