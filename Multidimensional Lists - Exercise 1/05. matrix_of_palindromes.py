rows, cols = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    curr_row = []
    for col in range(cols):
        first_el = chr(row+97)
        second_el = chr(row + col + 97)
        third_el = chr(row+97)

        element = str(first_el) + str(second_el) + str(third_el)

        curr_row.append(element)
    print(' '.join([x for x in curr_row]))
