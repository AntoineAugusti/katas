# http://rosalind.info/problems/lexv/


def combinations(alphabet, n, acc='', res=[]):
    if n > 0:
        for c in alphabet:
            res.append(acc + c)
            combinations(alphabet, n - 1, acc + c, res)

    return '\n'.join(res)

alphabet, size, _ = open("rosalind_lexv.txt", "r").read().split('\n')

print combinations(alphabet.split(), int(size))
