seq_one = {int(x) for x in input().split()}
seq_two = {int(n) for n in input().split()}

n = int(input())

for _ in range(n):
    command = input().split()

    if command[0] == "Add":
        if command[1] == "First":
            for i in command:
                if i.isdigit():
                    seq_one.add(int(i))
        elif command[1] == "Second":
            for j in command:
                if j.isdigit():
                    seq_two.add(int(j))

    elif command[0] == "Remove":
        if command[1] == "First":
            for i in command:
                if i.isdigit():
                    if int(i) in seq_one:
                        seq_one.remove(int(i))
        elif command[1] == "Second":
            for j in command:
                if j.isdigit():
                    if int(j) in seq_two:
                        seq_two.remove(int(j))

    elif command[0] == "Check":
        if command[1] == "Subset":
            is_sup_set = seq_one.issuperset(seq_two)

            print(is_sup_set)

sorted_seq_one = sorted(seq_one)
sorted_seq_two = sorted(seq_two)

print(*sorted_seq_one, sep=", ")
print(*sorted_seq_two, sep=", ")
