text = input()

count_chars = {}

for ch in text:
    if ch not in count_chars:
        count_chars[ch] = 0
    count_chars[ch] += 1

sorted_dict = {key: count_chars[key] for key in sorted(count_chars.keys())}

for key, value in sorted_dict.items():
    print(f"{key}: {value} time/s")
