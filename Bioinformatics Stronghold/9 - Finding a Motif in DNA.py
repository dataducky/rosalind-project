import re

DNAstr = "TGAATAAATAATAAATTGAATGAATAAATAATAAATCATCAAATAAATTGCGAAATAAATAATAATAAATTATGGAATAAATCTCAAATAAATAAGAATAAATGTGTTAATGACATGCAATAAATGAATAAATTTGAATAAATCAATAAATCAATAAATAAATAAATAAATAAATAAATAAATTGTCCTAGAGAATAAATAATAAATAATAAATGTAGACAATAAATCAATTGGCAATAAATGCAATAAATGCAATAAATAATAAATAATAAATCTAATAAATAATAAATTTCGGAATAAATGCCTTAATAAATTTAAATAAATCAATAAATCAATAAATAAAATCTAATAAATATAATAAATAATAAATCTCAATAAATAATAAATTAAGATAATAAATTTGGAAATAAATGAATAAATAAATAAATGAGAATAAATACAATAAATGAATAAATATCAAATAAATGAAAATAAATCCAAAATAAATATAATAAATGAATAAATAATAAATGTAGCGAATAAATCCGGTTAATAAATAATAAATCAATAAATAATAAATGAAATAAATTGAGTAATAATAAATGGAATAAATAATAAATGAATAAATAATAAATAAAATAAATAATAAATCATCAAAATAAATCCGAATAAATAGGAGGTCAATAAATGAATAAATAATAATAAATTCCCGAAATAAATAATAAATAGGTGATAATAAATACACGCAAATAAATAATAAATGAATAAATAAATAAATCGGCGAAATAAATAATAAATATCAAATAAATGTATGAATAAATATCTGAATAAATAATAAATATGTCGAATAAATAAAAATAAAT"
MOTIFstr = "AATAAATAA"
MotifPointList = []

TEMPstr = ""
for i in DNAstr:
    TEMPstr += i
    searchvar = rf'{MOTIFstr}$'
    testvar = re.search(searchvar, TEMPstr)
    if testvar is not None:
        spanvar = testvar.span()
        MotifPointList.append(spanvar[0]+1) 

endprint = ""
for i in MotifPointList:
    endprint += str(i)+" "
print(endprint)

    
    
    
    

print(searchvar)
print(DNAstr[824:835])


