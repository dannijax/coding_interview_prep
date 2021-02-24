## find n words before and after a word 

def binary_search(struct, mssg):
    high = len(struct) -1
    low = 0

    if high >= low :
        mid = (high + low) //2
        if struct[mid] == mssg:
            return mid
        

        