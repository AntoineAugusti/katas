# http://rosalind.info/problems/iprb/

f = open("rosalind_iprb.txt", "r")
for content in f:
    dominant, hetero, recessive = [float(x) for x in content.split()]

total = dominant + hetero + recessive

# Two recessive organisms
doubleRecessive = (recessive / total) * ((recessive - 1) / (total - 1))
# Two heterozygous organisms
doubleHetero = (hetero / total) * ((hetero - 1) / (total - 1))
# hetero + recessive
heteroRecessive = (hetero / total) * (recessive / (total - 1)) + (recessive / total) * (hetero / (total - 1))

totalRecessive = doubleRecessive + doubleHetero * 1/4 + heteroRecessive * 1/2
print (1 - totalRecessive)
