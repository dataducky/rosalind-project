DNAstr = "AACGAACACACCTTAACCAACGGCGTCCCTTGCTCTGCTGTGTAAAGGGCACCTTCCTTTACGCAACGACGAGTGGAAGAGGCCTTTGCTGCTTGATAATACCCAGCAGCAGCCGCATACAAGAGAATACAGCTTATCATCTATTGCCAGCCCTACAGCGTGCGGTAAAATATGCGTTACTCGCTCCTCTCATGTTGAAGAGGCGGATTAGCGCTTACCGTTCGCGGGGCGCTCCGCTTCAGGAGGGCAAATAACTAAGGTTTCATCCTGGGAATTGTCACAACATCTGTCTCCTGAACCACAAACCCCTAAATACGGTAGCGTTTACTCGTATCAAGCGACGCGGCTTAGCCATGGTGGATGATAGGCACACGTCAATATCGCGCGTTGCGCCCGTGGAGGACCTCCTGTGATAGACAAGCTCGTATAATCGTCGCGGGTCTTAACTAAGCGTTTATGATCTTTACATGACCTATTCGAATATTATAAGTAGACTACCCATAGGGTGTATATCTTGTACCCCTTCAGAAGAACGTAAGTATAGGTGAGAAATAGTTAGTTCAGCGTCGCCCGGCCGATCACGTAGGAACATAGAGAATTTAGTGGCGTAGGACGGCAGGCTGGATTCGTCATCAAGAGCGCACTACCGAATAAGAGCACAGCCAGTAGCGGGAAGAGCGCCATCTCCAGTGATATTCTGGACCGGTTTTGTCTGTAGACTCTCGCAACGACGATGTTATTAATAGTCCGTTGGTACGTAAAGGATTCAGGGTTTGTTCGCCGTAGAGTTAGCTGCGACGCGCGGGGTTCCAGTTCGCGTCACGAAAACCACGATAGCAAAATGACATGTTAACACCCTACCGCATAGAAATCGACTATTGTGCGAAAGACTACATCGCAGGCGCGGCCCATGGACATACCTCGGGAAGTTCTTTGCTCTTTTATTTAAAGTCGAGAAAT"
RNAstr = ""
ctr = 0
for i in DNAstr:
    if i == "T":
        RNAstr += "U"
    else:
        RNAstr += i
    ctr += 1
print(RNAstr)