def func_executor(*args):
    result = []

    for function_name, arguments in args:
        result.append(f"{function_name.__name__} - {function_name(*arguments)}")

    return '\n'.join(result)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2
