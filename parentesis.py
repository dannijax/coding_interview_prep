from collections import deque

def find_matching_bracket(sentence, opening_paren_index):
    open_nested_parnns = 0
    for position in range(opening_paren_index-1 , len(sentence)):
        chars = sentence[position]
        if chars == '(':
            open_nested_parnns +=1  
        elif chars == ')':
            if open_nested_parnns == 0:
                return position
            else:
                open_nested_parnns -= 1

    raise Exception("No closing parenthesis :(")


def find_matching(s, pos):
    stack = deque("")
    match_position = 0

    for position in range(pos -1, len(s)):
        if s[position] == '(':
            stack.append('(')
        elif s[position] == ')':
            if not stack:
                raise Exception("No closing parenthesis :(")
            else:
                elem = stack.pop()
                if elem == '(':
                    match_position  = position
        #print('position {0} shows {1}'.format(position, stack))
        #print(stack)


    return match_position


lez = find_matching('Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.', 10)
lez2 = find_matching('((((()))))', 2)

print(lez2)


