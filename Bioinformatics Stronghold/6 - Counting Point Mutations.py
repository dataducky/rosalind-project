strandS = "CGGTTACGTACGTATTAAAATTACCATGAGGTAAGACCGGGTAGGCTCGAGTCCCCCGCAATAAGGATGGGACGAATCGCGTGTGTGCTAGGGCTTTGGAGCCCCCACTCTACGGAGGATAAGGAGTATCCCTTGGCCATACGCGGCACCAATCGGGGACATCGAAATGGATATGGTAGCTGACTTTTTGCTCGCACCTTAAGACGCGTTTCGAGACACATGGGAACACGGTTGTGCCTTAGGACCCTGGCCAGAGACTGGAGTGCACTAGTATGATCGTATTTAGCTCCCGAAACGGAATCGGAGTAACAACTAACGTTACGATACAAATCGTTATGCACCATTTCAAATGGAATTAAGTGCTGCGACTAACAAGAGAGAAATTACCTTTCGGTGTTGGAAAGTATGTTGAAGACACCTGAGGACCAGAGGGCAAGACTTGTCGCCACGAGTTTCTTAATCGACTCTCCCGCGAAAGTCTGGTACCTACAGTTATTAATCTCTTTCACTGTAATCAATCCAAGGGACATTTGAAATCCGCGACAGGTGGGTCTGCCATATGTTATCGCCCCTATATTGAGCGATTCTAATGCTGCGCCTCTCTTCGTTGATGCCGGGTATTAAGGCCTATCACTACACGTACACATATGGGCAGGATCAACCGGTCACGTACCTCAAATGAAGCTAAACAAAACTCCTGGCTAATTTTGGAACAGGAGTATGATAGACCGCAGGCGGCCCGCATATCTCACCCCCGCGACGTACAACAGAGTGTTGGCTGGGGATCACAATATTTGTATAGCGTACTCCCATTAAAACAAAATCGCCACTTTTGAAACCACAGGCAGCGTTAAACCAAGCGCAGCACGTTAGCTTGCAGCAAGGGCCAGACGAGAGGCATACTACAG"
strandT = "CTATTGCGCACGGATTAAATAGACCAGCAGGGAAAAGATGGGACGCTCTTGAGCACATCGAAGAAGGCTCGATTTTTCCCGATTGTTCTAGGCCTTTTGATCCCCTAGTCACCGTAGGAGAAAGTATGGCGTACAGCAGGACGAGGCATCACTCGGGGACAGTTAAGCGCATAGAGTACCATACGTTTTGCTCGGCTCGCAATACACGGGTTTTGCCACTTGCGAAGTAGGATGTGCCTGCCATGTCTCGGGACACACTGCGATCCCCCAGTCCAGGCGCGATGCACTCCTGAGACATTTGCGCACCGTCGGGCGCTCTTACCATACACGTGGTTCTGCCCTAATTCAACTGAACCGTGATGCCCCGCCTCACGGGGGACTGTTCCCCTTCACCCGTATGGTCGCTGCTGGAACGCATAAGTCGACCAGATCGGAAACTATGTGCTAACTTGTCCAGAATACAAGCCACGCTCTAAATTCGCAATCTTCTAGTGCTTCTTAACTATGACTGCAATGCCCAGCACTTCCATACTTAGTGTCTTCAGTCTCCAGCTGACAGAACCCACGTTGCCACTATTTAGAGGTTGCCCTCCTGTCGGCCTACTTCTTGAGCGTATCCGTGCAAACTTGAACTACCACATGATGTCATGGGGTGCGTCCTACACTAACGCAGTGCGATCGCATAAAAATACTCGCATCAGGCCATTGCGGTTCAGGAGTGAGAACCCTCCCGAGAAGGCAACATAAGCGGTTGCCTGGAGGTCCAACAGAGGGATGCCCGAGTTCCCCTAAGTTTCTATTGAGGCGAGCCTGGGCACCAATGCGAGGATTGTATAAACCTGACCTCACGTCAATACCAATGCGTGACGGTCTACTTCGGCGAGCGGCGTACACGTACGTGGAGATCG"
ctr, hammingDistance = 0, 0
for i in strandS:
    if strandS[ctr] != strandT[ctr]:
        hammingDistance += 1
    ctr += 1
print(str(hammingDistance)) 