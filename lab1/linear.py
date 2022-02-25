def linear_search(A,target):
    for element in A:
        if element == target:
            return A.index(element)
    return -1