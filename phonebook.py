import sys

def find(data, key):
    return '{key}={value}'.format(key=key, value=data[key] ) if key in data else 'Not found'

n = 0
keys = []
phone_book = {}
for line in sys.stdin:
    if line.strip("\n").isdigit():
        n = int(line)
    elif len(line.split(" ")) == 2:
        phone_book[line.split(" ")[0].strip("\n")] = line.split(" ")[1].strip("\n")
    else:
        keys.append(line.strip("\n"))
        
for x in keys:
    print(find(phone_book, x))