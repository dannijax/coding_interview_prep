def shift_left(arr):
    count = 0
    if len(arr) < 2:
        return arr

    for i in range(len(arr)):
        
        if arr[i] != 0:
            arr[count] = arr[i] 
            count +=1
            

    while count < len(arr): 
        arr[count] = 0
        count += 1

    count = 0
    for i in range(1, len(arr)):
        print('{0} {1}'.format(count, i))
        if arr[count] == arr[i] and arr[count] != 0 or arr[i] != 0:
            arr[count] = arr[i] + arr[count + 1]
            arr[i] = 0
        count +=1
    return arr


# print(shift_left([1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]))
print(shift_left([0, 1, 1, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]))