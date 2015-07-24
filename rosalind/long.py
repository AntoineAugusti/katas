# http://rosalind.info/problems/long/


def superstring(arr, accumulator=''):
    # We now have all strings
    if len(arr) == 0:
        return accumulator

    # Initial call
    elif len(accumulator) == 0:
        accumulator = arr.pop(0)
        return superstring(arr, accumulator)

    # Recursive call
    else:
        for i in range(len(arr)):
            sample = arr[i]
            l = len(sample)

            for p in range(l / 2):
                q = l - p
                if accumulator.startswith(sample[p:]):
                    arr.pop(i)
                    return superstring(arr, sample[:p] + accumulator)
                if accumulator.endswith(sample[:q]):
                    arr.pop(i)
                    return superstring(arr, accumulator + sample[q:])

f = open("rosalind_long.txt", "r")
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

print superstring(dnas.values())
