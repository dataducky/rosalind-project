k = 27 # Homozygous dominant
m = 25 # Heterozygous
n = 27 # Homozygous recessive
total = k + m + n
#Probability two randomly selected mates will possess a dominant allele:
# Selecting the first mate
firstDomProb = k / total
firstHetProb = m / total
firstRecProb = n / total
# Selecting the second mate given the first mate
FDsecondDomProb = (((k - 1) / (total-1)))
FHsecondHetProb = ((m - 1) / (total-1))
FRsecondRecProb = ((n - 1) / (total-1))
secondDomProb = (k / (total-1)) # only possible if first mate isn't homozygous dominant
secondHetProb = (m / (total-1)) # only possible if first mate isn't heterozygous
secondRecProb = (n / (total-1)) # only possible if first mate isn't homozygous recessive
# Punnett Squaring : 6 possible mating outcomes, probability of dominant
DomDom = 1.0
DomHet = 1.0
DomRec = 1.0
HetHet = 0.75
HetRec = 0.5
RecRec = 0.0
# Summed probabilities
FDdomProb = ((firstDomProb*FDsecondDomProb*DomDom)+(firstDomProb*secondHetProb*DomHet)+(firstDomProb*secondRecProb*DomRec))
FHdomProb = ((firstHetProb*secondDomProb*DomHet)+(firstHetProb*FHsecondHetProb*HetHet)+(firstHetProb*secondRecProb*HetRec))
FRdomProb = ((firstRecProb*secondDomProb*DomRec)+(firstRecProb*secondHetProb*HetRec)+(firstRecProb*FRsecondRecProb*RecRec))
childDominantProb = (FDdomProb+FHdomProb+FRdomProb)
print(str(childDominantProb))