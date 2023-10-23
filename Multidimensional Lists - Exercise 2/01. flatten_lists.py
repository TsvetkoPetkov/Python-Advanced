numbers = input().split("|")

flatten = []

for sub_string in numbers[::-1]:
    if sub_string:
        flatten.extend(sub_string.split())

print(*flatten)
