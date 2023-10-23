number_of_students = int(input())

grades_dict = {}

for _ in range(number_of_students):
    student, grade = input().split()

    if student not in grades_dict:
        grades_dict[student] = []

    grades_dict[student].append(float(grade))

for key, value in grades_dict.items():
    print(f"{key} -> {' '.join(str(f'{x:.2f}') for x in value)} (avg: {sum(value) / len(value):.2f})")
