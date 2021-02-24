def get_slice(items):
    for i in range(len(items) + 1):
        for j in range(1, len(items) -i +1):
            yield (items[i:i+j])


x = [i for i in range(5)]

sub_array = [i for i in get_slice(x)]
sub2 = [i for i in get_slice([0, 0, 1])]
print(len(sub2))

def find_abs_diff(a, b):
    print('{0} {1} : {2} '.format(a, b, abs(a-b)))
    return abs(a-b)

def has_target(arr, target):
        low = 0
        high = len(arr) -1
        while low < high:
            if abs(arr[low]- arr[high]) == target:
                return True
            else: 
                low +=1
        return False


#print(has_target([1,1,3,4,5,6,7], 0) )