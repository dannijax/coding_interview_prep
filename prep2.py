def shift(arr):
    i = 0
    while i < len(arr):
        
        if arr[i] == 0:
            print(arr[i])
            #print(i)
            if len(arr) > i +1:
                arr[i +1] = 0
                i +=2

        i +=1

    print(arr)



shift([1,0,2,3,0,4,5,0])