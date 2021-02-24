class LinkedList(object):
    """
    docstring
    """
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next



list = LinkedList("Danijax", None)
print(list.next_node)

def is_isomorphic(s, t): 
    data = {}
    if len(s) != len(t):
        return False

    for c, d in zip(s,t):
        if (c in data) : 
            if data[c] != d:
                return False
        else:
            data[c] = d
    print(data)
    return True


#print(is_isomorphic("brian", "space"))

def pattern_recognize(str):
    arr = []
    key, value = str.split(';')
    print(key)
    values = value.split('|')
    for el in values:
        if not key:
            arr.append(0)
        else:
            arr.append(el.count(key))

    arr.append(sum(arr))
    print("|".join("{0}".format(n) for n in arr))


pattern_recognize('bc;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32')
pattern_recognize('aa;aaaakjlhaa|aaadsaaa|easaaad|sa')

pattern_recognize('b;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32')
pattern_recognize(';bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32')

def is_palindrome(str):
    return str == str[:: -1]

print(is_palindrome('madame'))


