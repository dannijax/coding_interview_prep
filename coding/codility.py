ighdef solution(ranks):
    reports = {}
    for x in ranks:
        if x + 1 in ranks:
            if x in reports:
                r = reports[x]
                reports[x] = r+1
            else:
                reports[x] = 1
    return sum(reports.values())

print(solution([3,4,3, 0,2,2, 3,0,0]))

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

print(solution_a('AABBBB'))