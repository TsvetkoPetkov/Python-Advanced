from collections import deque

tools = deque([int(x) for x in input().split()])
substances = deque([int(x) for x in input().split()])
challenges = deque([int(x) for x in input().split()])

while tools and substances and challenges:
    first_tool = tools[0]
    last_substance = substances[-1]

    result = first_tool * last_substance

    is_resolved = False

    for challenge in challenges:
        if result == challenge:
            tools.popleft()
            substances.pop()
            challenges.remove(challenge)
            is_resolved = True
            break

    if not is_resolved:
        tools.popleft()
        tools.append(first_tool + 1)
        substances.pop()
        if (last_substance - 1) != 0:
            substances.append(last_substance-1)

    if challenges:
        if not tools or not substances:
            print("Harry is lost in the temple. Oblivion awaits him.")
            break
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")


if tools:
    print(f"Tools: {', '.join([str(x) for x in tools])}")

if substances:
    print(f"Substances: {', '.join([str(x) for x in substances])}")

if challenges:
    print(f"Challenges: {', '.join([str(x) for x in challenges])}")
