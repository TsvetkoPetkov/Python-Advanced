n = int(input())

max_size = -10000
longest_intersection = set()

for _ in range(n):
    range_one, range_two = input().split("-")

    splitted_range_one = [int(x) for x in range_one.split(',')]
    splitted_range_two = [int(x) for x in range_two.split(',')]

    first_set = set()
    second_set = set()

    for i in range(splitted_range_one[0], splitted_range_one[1]+1):
        first_set.add(i)

    for i in range(splitted_range_two[0], splitted_range_two[1]+1):
        second_set.add(i)

    intersection = first_set.intersection(second_set)

    if len(intersection) > max_size:
        max_size = len(intersection)
        longest_intersection = intersection

print(f"Longest intersection is {list(longest_intersection)} with length {max_size}")
