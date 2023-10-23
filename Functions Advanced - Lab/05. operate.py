def operate(operator, *args):
    if operator == "+":
        return sum(args)

    elif operator == "-":
        total = int(args[0])
        for el in range(1, len(args)):
            total -= args[el]

        return total

    elif operator == "*":
        total = 1
        for el in args:
            total *= el
        return total

    elif operator == "/":
        total = int(args[0])
        for el in range(1, len(args)):
            total /= args[el]

        return total
