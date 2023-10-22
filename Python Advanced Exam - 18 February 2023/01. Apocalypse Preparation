from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = deque([int(x) for x in input().split()])

patches_counter = 0
bandage_counter = 0
medKit_counter = 0

while textiles and medicaments:
    first_textile = textiles[0]
    last_medicament = medicaments[-1]

    current_sum = first_textile + last_medicament

    if current_sum == 30:
        patches_counter += 1
        textiles.popleft()
        medicaments.pop()
    elif current_sum == 40:
        bandage_counter += 1
        textiles.popleft()
        medicaments.pop()
    elif current_sum == 100:
        medKit_counter += 1
        textiles.popleft()
        medicaments.pop()
    elif current_sum > 100:
        remaining = current_sum - 100
        medKit_counter += 1
        textiles.popleft()
        medicaments.pop()
        medicaments.append(remaining + medicaments.pop())
    else:
        textiles.popleft()
        medicaments.pop()
        medicaments.append(last_medicament + 10)

my_dict = {
    "MedKit": medKit_counter,
    "Bandage": bandage_counter,
    "Patch": patches_counter
}

if not medicaments and not textiles:
    print("Textiles and medicaments are both empty.")

elif not textiles:
    print("Textiles are empty.")

elif not medicaments:
    print("Medicaments are empty.")

sorted_dict = sorted(my_dict.items(), key=lambda kvp: (-kvp[1], kvp[0]))

output = ""

for textile, medicament in sorted_dict:
    if medicament > 0:
        output += f"{textile} - {medicament}\n"

if output:
    print(output.strip())

if medicaments:
    print(f"Medicaments left: {', '.join([str(x) for x in reversed(medicaments)])}")

if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
