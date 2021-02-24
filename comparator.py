import functools

def compare(x1, x2):
    if x2 %2 == 0 and x1 > x2:
        return 1
    elif x1%2 ==0 and x2 < x1:
        return -1
    else:
        return 0


print(compare(2, 3))

x =  [i for i in range(0, 50)]
#print(x)
y = sorted(x, key=functools.cmp_to_key(compare))
print(y)


arr = [i for i in x if i%2 == 0] + [i for i in x if i%2 == 1]
    

print(arr)

