import timeit

def solution(arr):
    g = find_largest(arr)
    #print('gr: '+ str(g + 2))
    if g <= 0:
        return 1
    for x in range(1, g + 2):
        if x not in arr:
            return x
    



    


def find_largest(arr):
    arr.sort()
    return arr[-1]


#solution([-1, -2, 5, 6, 9])
#solution([1, 3, 6, 4, 1, 2])
#print(solution([-1, -2, 5, 6]))rt

print(solution([1, 3, 5, 6, 4, 1, 2]))


print(solution([-1, -2, -3]))

##Given an array A of N integers, return true if A contains at least two elements which differ by 1, and false otherwise.
def soln_1(arr):
    if len(arr) <= 1:
        return False
    data = set()
    for n in arr:
        if n+1 in data or n-1 in data:
            return True

        data.add(n)
    return False

print(soln_1([4, 10, 8, 5, 9]))

#Possible solution that does not use map/set:

###Sort input array O(n logn)
#Run the array from i = 1 to the end.
#if (Math.abs(A[i] - A[i-1]) == 1) return true

##Write a function that returns the maximum possible value obtained by inserting one '5' digit inside the decimal representation of integer N.

def max_possible_value(num):
    res = str(num)
    items  = list(res)
    if num < 0:
        for index in range(len(items)):

            if res[index].isnumeric() and int(res[index])> 5:
                items.insert(index, '5') 
                return str(items)

    else:
        for index in range(len(items)):

            if int(res[index])<5:
                items.insert(index, '5') 
                return str(items)


def reverse(arr):
    for index in reversed(range(len(arr))):
        yield index, arr[index]

its = ['-','6', '6']

for index, ite in reverse(its):
    print(ite, index)



print(max_possible_value(-661))
print(max_possible_value(1234))
print(max_possible_value(7643))
print(max_possible_value(0))

    



