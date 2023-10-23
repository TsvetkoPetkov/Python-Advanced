from collections import deque

materials = deque(int(x) for x in input().split())
magic = deque(int(x) for x in input().split())

done = []
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while materials and magic:
    material = materials.pop() if magic[0] or not materials[0] else 0
    magic_level = magic.popleft() if material or not magic[0] else 0

    if not magic_level:
        continue

    product = material * magic_level

    if presents.get(product):
        done.append(presents[product])
    elif product < 0:
        materials.append(material + magic_level)
    elif product > 0:
        materials.append(material + 15)

if {"Doll", "Wooden train"}.issubset(done) or {"Teddy bear", "Bicycle"}.issubset(done):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")

if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

[print(f"{toy}: {done.count(toy)}") for toy in sorted(set(done))]
