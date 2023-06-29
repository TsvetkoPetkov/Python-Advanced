def age_assignment(*args, **kwargs):
    result = []
    for name in args:
        for letter, years in kwargs.items():
            if name[0] == letter:
                result.append(f"{name} is {years} years old.")

    output = ''
    for el in sorted(result):
        output += el + "\n"

    return output[:-1]
