from collections import deque
from typing import Type

parenthesis = deque(input())
open_brackets = deque()

while parenthesis:
    current_bracket = parenthesis.popleft()

    if current_bracket in '({[':
        open_brackets.append(current_bracket)
    elif not open_brackets:
        print("NO")
        break
    else:
        if (open_brackets.pop() + current_bracket) not in "()[]{}":
            print("NO")
            break
else:
    print("YES")
