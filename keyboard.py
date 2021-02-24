def count(keyboard, text ):
    key_map = {char: i for i, char in enumerate(keyboard)} 

    if len(text) >1:
        mid = len(text) // 2
        l = text[:mid]
        r = text[mid:]

    curr_position = 0
    result = 0
    for char in text:
        diff = abs(key_map[char] - curr_position)
        result += diff 
        curr_position = key_map[char]
    return result, curr_position


print(count('abcdefghijklmnopqrstuvwxy', 'cba'))



