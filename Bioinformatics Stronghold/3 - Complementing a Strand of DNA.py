DNAstr = "GTTAAAACTTACTGGAAATTTCCTTGCTAGAAGAATGATACTACGACCGGCCACATAAGTGTATTTTGCCGTCATTAGAGTCTCCCAGCCTCCTCGCTATCCGACAACTCTAGCGCGGTTCGCTCTGTTGGGTGCGTTTGTTGCATGCAATCGATACAGATACATCATGAATAGTGTATGCGTTGGTTCGGACCATTAACGTTCTCAGTGCTGCCTCAATAGTTTCTTTGCAGGGAATAGGTAAGGTCCCCTGCCTGGCGGAATTACGGGAAACGCAATCATGACGCTTAGGATATCGTAGCCAAGGGCCGTGCAAACAGTATAGAGATCATCGAGCTGAACCAATGCTGTTGCAGAACTTGCTCACTAATCTGAGCTAATTCCCGGCCCTTACTGAATGCAACATGCCCAGGTTATCTAGTATTGAGATATCCTGCCCGAATATCTACTGGCGGATGGCACTCGAGGATCCTCTTTGCTACGGATCCGGTATAGGATGTGCCCATAATTTGCTAGATTCTATTAGTTAACCGTCCGAGATGTACGCCCTCCTCAGTAAGATTCTGATACTCGCAGCTGAGTTAGCCACTACTGGAACCCGTAATGCATGTTGGCTTTACCTTGGAGCTCTTAGCCTTATACATGAGTGGGTATTAGCATATGCGCAGCGATAGTGCGTGGCACCTCAATCAAGGACGAGGTTGAAACTTTCTGGATCCGTAACGGCAAGGGATACCCTCTCTCTCAATATGCAGTAGCTCAAAGACTTCCACCGCAGGTATGGCGTGACGTGCCTATGTATGCTGGGTCACAAGCTGGACATTTGTGACAAAGAAATACGTGATGAATGATTACAATTACAGCACGCGTTCCGGCGACGGTCAGTGCTGATCTTCGCAGCTTTAAAAAGACAACAGTGCGTGACATTAGGACCAAACAGCGCTCTCGAAGGGAAGACCGTTCGGATCAACCACGTCGCCGCTGAT"
DNARvrsComp = ""
for i in reversed(DNAstr):
    if i == "A":
        DNARvrsComp += "T"
    if i == "C":
        DNARvrsComp += "G"
    if i == "G":
        DNARvrsComp += "C"
    if i == "T":
        DNARvrsComp += "A"
print(DNAstr)
print(DNARvrsComp)