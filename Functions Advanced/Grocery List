def shop_from_grocery_list(budget, grocery_list, *args):
    purchased = []

    for products in args:
        if budget <= 0:
            break
        name, price = products

        if name not in grocery_list:
            continue
        if name in purchased:
            continue
        if (budget-price) >= 0:
            budget -= price
        else:
            break

        grocery_list.remove(name)
        purchased.append(name)

    if len(grocery_list) == 0:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join([str(x) for x in grocery_list])}."
