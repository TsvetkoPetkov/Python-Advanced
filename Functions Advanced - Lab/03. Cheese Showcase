def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''

    for name, quantity in sorted_cheeses:
        result += name + "\n"
        reversed_q = sorted(quantity, reverse=True)
        for q in reversed_q:
            result += str(q) + "\n"

    return result[:-1]
