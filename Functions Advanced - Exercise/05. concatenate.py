def concatenate(*args, **kwargs):
    args_text = ''

    for word in args:
        args_text += word

    for key, value in kwargs.items():
        if key in args_text:
            args_text = args_text.replace(key, value)

    return args_text
