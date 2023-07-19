# multiply numbers in a list
def multiplyofnumbers(numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total    

print(multiplyofnumbers((4,3,3)))
print(multiplyofnumbers((10,10,10)))