def is_palindrome(word):
    start = 0
    end = len(word) -1
    progress = False
    while start < end:
        #print('{0} : {1}'.format(word[start], word[end]))
        progress = word[start].lower() == word[end].lower()
        start += 1
        end -=1

    return progress


def is_permut_palindrome(word):
    

print(is_palindrome('madam'))
print(is_palindrome('madamm'))
print(is_palindrome('Sagas'))
print(is_palindrome('Solos'))
print(is_palindrome('Repaper'))
print(is_palindrome('Kayak'))
print(is_palindrome('Wow'))
print(is_palindrome('ivicc'))
print(is_palindrome('civic'))
print(is_palindrome('112231032211'))
print(is_palindrome('1122332211'))
print(is_palindrome('112233211'))
