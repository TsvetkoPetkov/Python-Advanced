n = int(input())

my_stack = []

for i in range(n):
    command = input().split()

    if int(command[0]) == 1:
        number = int(command[1])
        my_stack.append(number)
    elif int(command[0]) == 2:
        if len(my_stack) > 0:
            my_stack.pop()
    elif int(command[0]) == 3:
        if len(my_stack) > 0:
            print(max(my_stack))
    elif int(command[0]) == 4:
        if len(my_stack) > 0:
            print(min(my_stack))

print(*my_stack[::-1], sep=", ")
