def grocery_store(**kwargs):
    sorted_products = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    result = ''

    for product, value in sorted_products:
        result += (f'{product}: {value}\n')

    return result[:-1]
