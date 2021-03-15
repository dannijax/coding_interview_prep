def min_swap(arr):
    swaps = 0
    data = dict(zip(arr, range(1,len(arr)+1)))
    for i in range(1,len(arr)+1):
        if data[i] != i:
            data[arr[i-1]]=data[i]
            arr[data[i]-1]=arr[i-1]
            swaps+=1
    return swaps
print(min_swap([7,1,3,2,4,5,6]))