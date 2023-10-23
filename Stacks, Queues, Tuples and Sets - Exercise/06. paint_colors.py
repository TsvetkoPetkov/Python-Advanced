from collections import deque

color_words = deque(input().split())

colors = {'red', 'blue', 'yellow', 'green', 'purple', 'orange'}

sec_colors = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'yellow', 'blue'},
}

output = []

while color_words:
    first_word = color_words.popleft()
    second_word = color_words.pop() if color_words else ""

    for element in (first_word + second_word, second_word + first_word):
        if element in colors:
            output.append(element)
            break
    else:
        for element in (first_word[:-1], second_word[:-1]):
            if element:
                color_words.insert(len(color_words) // 2, element)

for color in set(sec_colors.keys()).intersection(output):
    if not sec_colors[color].issubset(output):
        output.remove(color)

print(output)
