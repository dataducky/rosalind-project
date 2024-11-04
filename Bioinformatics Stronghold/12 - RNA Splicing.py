import re
import pandas as pd
#initalize values
DNAdict = {}
count, lineCount, lineTotal = 0, 0, 0
match = r'^>'
strID = ""
strand = ""
#counts total lines
with open(r"12inputfile.txt", 'r') as totaler:
    lineTotal = len(totaler.readlines())

#Opens the input file and scans each line. Saves FASTA format text files into a dictionary(DNAdict)
GCinput = open('12inputfile.txt','r')
for line in GCinput:
    #Keeps track of line count, adds one per line
    lineCount += 1
    #If the line starts with regex r'^>'
    if re.match(match, line):
        #Saves strand to strID in DNAdict when the strand is full
        if strand != "":
            DNAdict[strID] = strand
        #initializes strand ID to save to DNAdict
        strID = line[1:].strip() 
        # ending sequence, clears strand to empty string
        strand = ""
    else: #Because line does not start with '>', the line must be part of the strand, and is added to the strand string.
        strand += line.strip()
    #Saves strand to strID in DNAdict at the end of the loop function
    if lineCount == lineTotal:
        DNAdict[strID] = strand
GCinput.close()

#identifies the DNA string(thus assigning the compliment as introns)
largestStr, DNAStrIndex, ctr = 0, 0, 0
for i in DNAdict:
    if len(DNAdict[i]) > largestStr:
       largestStr = len(DNAdict[i])
       DNAStrIndex = ctr
       DNAStrKey = i
    ctr += 1

#Removes introns from DNA string, creating the spliced coding strand
codingStrand = str(DNAdict[DNAStrKey])
splicedDNA = codingStrand
ctr = 0
for i in DNAdict:
    if ctr == DNAStrIndex:
        pass
    else:
        splicedDNA = splicedDNA.replace(str(DNAdict[i]), '')
    ctr += 1

#Translate coding strand into RNA
mRNAStrand = splicedDNA.replace("T","U")

# Creates a dictionary of codons for RNA to amino acid
codonlist = "UUU F      CUU L      AUU I      GUU V UUC F      CUC L      AUC I      GUC V UUA L      CUA L      AUA I      GUA V UUG L      CUG L      AUG M      GUG V UCU S      CCU P      ACU T      GCU A UCC S      CCC P      ACC T      GCC A UCA S      CCA P      ACA T      GCA A UCG S      CCG P      ACG T      GCG A UAU Y      CAU H      AAU N      GAU D UAC Y      CAC H      AAC N      GAC D UAA Stop   CAA Q      AAA K      GAA E UAG Stop   CAG Q      AAG K      GAG E UGU C      CGU R      AGU S      GGU G UGC C      CGC R      AGC S      GGC G UGA Stop   CGA R      AGA R      GGA G UGG W      CGG R      AGG R      GGG G"
codonDict = {}
dictKey = ""
for i in codonlist.split(" "):
    if re.search("\w{1}", i): #checks for existance of characters in line
        if len(i) == 3: #keys(codons) are three characters
            dictKey = i
        if len(i) == 1 or len(i) == 4: #values(amino acids) are single letters or 'Stop'
            codonDict[dictKey] = i

#Translates the mRNA into protein
transcribedstr = ""
currentcodon = ""
Transcripting = False
for i in mRNAStrand:
    currentcodon += i
    startCodon = re.search("AUG", currentcodon)
    if startCodon != None and Transcripting == False:
        Transcripting = True
        currentcodon = ""
        transcribedstr += "M"
    if Transcripting == True:
        if len(currentcodon) == 3:
         for key,value in codonDict.items():
          if currentcodon == key:
           if value == "Stop":
            break
           transcribedstr += value
           currentcodon = ""
    
print(transcribedstr)