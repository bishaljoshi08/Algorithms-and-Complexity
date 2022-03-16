def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
    return A

if __name__ == '__main__':
    a = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print(insertion_sort(a))