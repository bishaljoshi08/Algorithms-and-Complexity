def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
        return A

def merge(A, p, q, r):
    L = A[p : q+1]
    R = A[q+1 : r+1]
    i = j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
            if i >= len(L) and j < len(R):
                for m in range(k + 1, r + 1):
                    # print('b')
                    A[m] = R[j]
                    j += 1  
                return A
        else:
            A[k] = R[j]
            j += 1
            if j >= len(R) and i < len(L):
                for n in range(k + 1, r + 1):
                    # print('a')
                    A[n] = L[i]
                    i += 1
                return A
    return A

# if __name__ == '__main__':
#     a = [9, 1, 8, 2, 7, 3, 6, 4, 5]
#     print(merge(a, 0, 4, 8))
#     b = [1, 2, 4, 8, 10, 0, 3, 6, 5]
#     print(merge_sort(b, 0, 8))

