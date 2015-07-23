# http://rosalind.info/problems/orf/

DNA_CODON_TABLE = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}


def translateCodon(codon):
    if len(codon) != 3:
        return None
    protein = DNA_CODON_TABLE[codon]
    return protein


def reverseComplement(dna):
    lookup = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([lookup[c] for c in reversed(dna)])


def possibleProteinStrings(s):
    results = []
    indices = []

    l = len(s)
    for i in range(l):
        protein = translateCodon(s[i:i+3])
        if protein is not None and protein == 'M':
            indices.append(i)

    for i in indices:
        stopFound = False
        proteinString = ''

        for j in range(i, l, 3):
            protein = translateCodon(s[j:j+3])
            if protein is None:
                break

            if protein == 'Stop':
                stopFound = True
                break

            proteinString += protein

        if stopFound:
            results.append(proteinString)

    return results


f = open("rosalind_orf.txt", "r")

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

possibilities = possibleProteinStrings(dnas[currentKey])
reversedDna = reverseComplement(dnas[currentKey])
reversePossibilities = possibleProteinStrings(reversedDna)
possibilities = possibilities + reversePossibilities
print "\n".join(set(possibilities))
