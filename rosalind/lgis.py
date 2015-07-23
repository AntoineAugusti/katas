# http://rosalind.info/problems/lgis/


def reduceFromMax(m, lst):
    max_value = max(m)

    result = []
    for i in range(len(m)):
        if max_value == m[i]:
            result.append(lst[i])
            max_value -= 1

    return result


def LIS(A):
    m = [0] * len(A)
    for x in range(len(A)-2, -1, -1):
        for y in range(len(A)-1, x, -1):
            if m[x] <= m[y] and A[x] < A[y]:
                m[x] += 1

    # if A was [5, 1, 4, 2, 3],
    # m is now [0, 2, 0, 1, 0]

    return reduceFromMax(m, A)


def LDS(A):
    m = [0] * len(A)
    for x in range(len(A)-2, -1, -1):
        for y in range(len(A)-1, x, -1):
            if m[x] <= m[y] and A[x] > A[y]:
                m[x] += 1

    # if A was [5, 1, 4, 2, 3],
    # m is now [2, 0, 1, 0, 0]

    return reduceFromMax(m, A)

nb, lst, _ = open("rosalind_lgis.txt", "r").read().split('\n')
lst = map(int, lst.split())

print ' '.join(map(str, LIS(lst)))
print ' '.join(map(str, LDS(lst)))
