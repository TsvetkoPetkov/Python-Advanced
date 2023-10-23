numbers = [int(x) for x in input().split()]

def negatives(numbers):
    sum_negatives = 0
    for n in numbers:
        if n < 0:
            sum_negatives += n
    return sum_negatives


def positives(numbers):
    sum_positives = 0
    for n in numbers:
        if n > 0:
            sum_positives += n
    return sum_positives


print(negatives(numbers))
print(positives(numbers))

if abs(negatives(numbers)) > abs(positives(numbers)):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
