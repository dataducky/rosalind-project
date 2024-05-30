import re

# Creates a dictionary of codons for amino acid
codonlist = "UUU F      CUU L      AUU I      GUU V UUC F      CUC L      AUC I      GUC V UUA L      CUA L      AUA I      GUA V UUG L      CUG L      AUG M      GUG V UCU S      CCU P      ACU T      GCU A UCC S      CCC P      ACC T      GCC A UCA S      CCA P      ACA T      GCA A UCG S      CCG P      ACG T      GCG A UAU Y      CAU H      AAU N      GAU D UAC Y      CAC H      AAC N      GAC D UAA Stop   CAA Q      AAA K      GAA E UAG Stop   CAG Q      AAG K      GAG E UGU C      CGU R      AGU S      GGU G UGC C      CGC R      AGC S      GGC G UGA Stop   CGA R      AGA R      GGA G UGG W      CGG R      AGG R      GGG G"
codonDict = {}
dictKey = ""
for i in codonlist.split(" "):
    if re.search("\w{1}", i): #checks for existance of characters in line
        if len(i) == 3: #keys(codons) are three characters
            dictKey = i
        if len(i) == 1 or len(i) == 4: #values(amino acids) are single letters or 'Stop'
            codonDict[dictKey] = i


RNAstr = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
#currentcodon = ""
#for i in RNAstr:
    