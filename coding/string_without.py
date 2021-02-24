def solution(arg) :
    h = len(arg)
    max_count = 3
    prev_count = 1
    res = []

    for i in range(h):
        if(arg[i] == arg[i-1]): 
            prev_count +=1
        else:
            prev_count = 1
        
        if(prev_count < max_count):
            res.append(arg[i])
        
    return res


#print(solution("eedaaad"))

def solution_a(data):
    a_char = 'A'
    b_char = 'B'
    b_n = 0
    min_d = 0
    for i in data:
        if(a_char == i):
            min_d = min(b_n, min_d + 1)
        else:
            b_n +=1
    
    return min_d

print(solution_a('BAAABAB'))

    
    
