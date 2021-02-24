def find_repeat(numbers):

    # Find a number that appears more than once
    available = {}
    repeated = -1
    
    for x in range(len(numbers)):
        if numbers[x] in available:
            repeated = numbers[x]
        else:
            available[numbers[x]] = x 
    print(available)
    return repeated

print(find_repeat([1, 2]))
print(find_repeat([1, 2, 3, 2]))