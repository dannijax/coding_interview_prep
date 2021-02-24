from collections import Counter
def is_valid_palindrome(s: str) -> bool:
    count = Counter(s)
    return len([char for char, freq in count.items() if freq % 2]) <= 1

print(is_valid_palindrome('abba'))
print(is_valid_palindrome('mdaam'))
print(is_valid_palindrome('code'))
print(is_valid_palindrome('carerac'))


