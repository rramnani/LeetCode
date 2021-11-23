def BinarySearch(list, target):
    """ Takes a list of numbers as the input and returns the index if the
    target value is found in the list otherwise it returns None
    """
    first=0
    last=len(list) -1

    while first<=last:
        midpoint=(first+last)//2
        if list[midpoint] == target:
            return midpoint
        else:
            if list[midpoint] < target:
                first=midpoint+1
            else:
                last=midpoint-1
    return None

list = range(1,10, 1)
result = BinarySearch (list, 5)

print(*list, sep='\n')

print ("target found at: ", result)