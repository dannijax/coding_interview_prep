def solution(blocks):
    if len(blocks) <=2 :
        return 2
    else:
        return move_left(blocks)

def move_left(arr):
    l_index = []
    r_index = []

    for i in range(0, len(arr)):
        if arr[i] <= arr[i-1]:
            l_index.append(l_index[i -1] +1)

        else:
            l_index.append(0)

    for i in range(len(arr) -2, -1, -1):
        if arr[i] <= arr[i +1]:
            r_index[i] = r_index[i + 1] +1
        else:
            r_index[i] = 0

    total = 0

    for x in range(0, len(arr)):
        if (l_index[i] + r_index[i] > total):
            total = l_index[i] + r_index[i]
	
	return total + 1

print(solution([2,6,8,5]))
