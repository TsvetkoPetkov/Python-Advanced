n = int(input())

odd_set = set()
even_set = set()

row = 1

for _ in range(n):
    name = input()

    chars_sum = 0

    for ch in name:
        chars_sum += ord(ch)

    curr_total = chars_sum // row

    row += 1

    if curr_total % 2 == 1:
        odd_set.add(curr_total)
    else:
        even_set.add(curr_total)

sum_odd_set = sum(odd_set)
sum_even_set = sum(even_set)

if sum_odd_set == sum_even_set:
    union = odd_set.intersection(even_set)
    print(*union, sep=", ")

elif sum_odd_set > sum_even_set:
    diff = odd_set.difference(even_set)
    print(*diff, sep=", ")

elif sum_odd_set < sum_even_set:
    sym_diff = odd_set.symmetric_difference(even_set)
    print(*sym_diff, sep=", ")
