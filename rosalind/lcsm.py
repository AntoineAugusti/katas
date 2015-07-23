# http://rosalind.info/problems/lcsm/


def substrInEveryElement(arr, part):
    for dna in arr:
        if part not in dna:
            return False
    return True


def commonSubstring(arr, l):
    first = arr[0]
    for i in range(len(first)-l+1):
        part = first[i:i+l]
        if substrInEveryElement(arr, part):
            return part
    return ""


def longestCommonSubstr(arr):
    l = 0
    r = len(arr[0])

    while l+1 < r:
        mid = (l+r) / 2
        if commonSubstring(arr, mid) != "":
            l = mid
        else:
            r = mid

    return commonSubstring(arr, l)

f = open("rosalind_lcsm.txt", "r")

dnas = {}
currentKey = ''
for content in f:
    # Beginning of a new sample
    if '>' in content:
        key = content.rstrip().replace('>', '')
        currentKey = key
        dnas[currentKey] = ''
    else:
        dnas[currentKey] += content.rstrip()

print longestCommonSubstr(dnas.values())
