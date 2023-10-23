def even_odd(*args):
    if args[-1] == "even":
        return [int(num) for num in args[:-1] if int(num) % 2 == 0]
    elif args[-1] == "odd":
        return [int(num) for num in args[:-1] if int(num) % 2 != 0]
