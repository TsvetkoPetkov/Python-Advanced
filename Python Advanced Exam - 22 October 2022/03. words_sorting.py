def words_sorting(*args):
    word_dict = {}

    total_values_sum = 0

    for word in args:
        if word not in word_dict:
            word_dict[word] = 0

        word_dict[word] += sum([ord(char) for char in word])
        total_values_sum += sum([ord(char) for char in word])

    if total_values_sum % 2 == 0:
        return "\n".join(f"{w} - {v}" for w, v in sorted(word_dict.items(), key=lambda x: x[0]))
    else:
        return "\n".join(f"{w} - {v}" for w, v in sorted(word_dict.items(), key=lambda x: x[1], reverse=True))
