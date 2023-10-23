from collections import deque

expression = input()
open_brackets = deque()

for el in range(len(expression)):
    if expression[el] == "(":
        open_brackets.append(el)
    elif expression[el] == ")":
        start_inx = open_brackets.pop()
        end_inx = el
        print(expression[start_inx:end_inx+1])
