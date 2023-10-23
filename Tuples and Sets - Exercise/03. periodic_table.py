n = int(input())

unique_chemical_compounds = set()

for _ in range(n):
    chemical_compounds = input().split()
    for c in chemical_compounds:
        unique_chemical_compounds.add(c)

print(*unique_chemical_compounds, sep="\n")
