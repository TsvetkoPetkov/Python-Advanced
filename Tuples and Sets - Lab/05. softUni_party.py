number_of_guests = int(input())

invited_guests = set()

for _ in range(number_of_guests):
    code = input()
    invited_guests.add(code)

while True:
    guest = input()

    if guest == "END":
        break

    if guest in invited_guests:
        invited_guests.remove(guest)

print(len(invited_guests))

for code in sorted(invited_guests):
    print(code)
