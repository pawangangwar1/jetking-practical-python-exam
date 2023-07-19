# sum all the numbers in a list

def sumofnumbers(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

print(sumofnumbers((1,4,6,5,5)))
print(sumofnumbers((20,30,50)))    