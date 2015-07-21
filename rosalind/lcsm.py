# http://rosalind.info/problems/lcsm/


def substr_in_all(arr, part):
    for dna in arr:
        if part not in dna:
            return False
    return True


def common_substr(arr, l):
    first = arr[0]
    for i in range(len(first)-l+1):
        part = first[i:i+l]
        if substr_in_all(arr, part):
            return part
    return ""


def longest_common_substr(arr):
    l = 0
    r = len(arr[0])

    while l+1 < r:
        mid = (l+r) / 2
        if common_substr(arr, mid) != "":
            l = mid
        else:
            r = mid

    return common_substr(arr, l)

f = open("rosalind_lcsm.txt", "r")

lines = []
dnas = {}
currentKey = ''
for content in f:
    # We have a new sample, remember the one we are capturing
    if '>' in content:
        key = content.rstrip().replace('>', '')
        currentKey = key
        dnas[currentKey] = ''
    else:
        dnas[currentKey] += content.rstrip()

print longest_common_substr(dnas.values())
