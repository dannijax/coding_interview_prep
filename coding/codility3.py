def solution(blocks):
    if len(blocks) <=2:
        return 2
    l = move_left(blocks)
    r = move_right(blocks)
    return r -l + 1


def move_left(block):
    l_index = 0
    for i in range(len(block) -1, -1, -1):
        if i == 0:
            break
        if(block[i] <= block[i -1]):
            l_index = i -1
        else:
            l_index = i
    return l_index

def move_right(block):
    r_index = 0
    for i in range(0, len(block)):
        if i == len(block) -1:
            break
        if(block[i] <= block[i +1]):
            r_index = i + 1
        else:
            r_index = i
    return r_index

print(solution([1,5,5,2,6]))