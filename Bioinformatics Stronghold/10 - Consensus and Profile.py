import re
import pandas as pd
#initalize values
DNAdict = {}
count, lineCount, lineTotal = 0, 0, 0
match = r'^>'
strID = ""
strand = ""
#counts total lines
with open(r"10inputfile.txt", 'r') as totaler:
    lineTotal = len(totaler.readlines())


#Opens the input file and scans each line
GCinput = open('10inputfile.txt','r')
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

#---profile matrix portion---
#i is the strID, j is the strand.
# create dict
first_key = list(DNAdict.keys())[0]
strandLength = len(DNAdict[first_key]) - 1
strandList = []
indexCount = 0
for i in DNAdict[first_key]:
    strandList.append(0)
PROFDict = {"Astr":strandList, "Cstr":strandList,"Gstr":strandList,"Tstr":strandList}
ProfileMatrix = pd.DataFrame(data=PROFDict)
#for strand ID in dict
for i in DNAdict:
    nucCount = 0
    #for strand per strand ID
    for j in DNAdict[i]:
     #for nucleotide in each strand
     for nuc in j:
        #sorting statements
        if nuc == "A":
            ProfileMatrix.loc[nucCount, "Astr"] += 1
        if nuc == "C":
            ProfileMatrix.loc[nucCount, "Cstr"] += 1
        if nuc == "G":
            ProfileMatrix.loc[nucCount, "Gstr"] += 1
        if nuc == "T":
            ProfileMatrix.loc[nucCount, "Tstr"] += 1
        nucCount += 1

nucCount = 0
consensusString = ""
while nucCount <= strandLength:
    highestValue = 0
    consensusNuc = ""
    for i in ProfileMatrix:
        if ProfileMatrix[i][nucCount] > highestValue:
            highestValue = ProfileMatrix[i][nucCount]
            consensusNuc = i
    if consensusNuc == "Astr":
        consensusString += ("A")
    if consensusNuc == "Cstr":
        consensusString += ("C")
    if consensusNuc == "Gstr":
        consensusString += ("G")
    if consensusNuc == "Tstr":
        consensusString += ("T")
    nucCount += 1

    
print(consensusString)
APrint = "A: "
for i in ProfileMatrix.Astr:
    APrint += str(i) + " "
print(APrint)
CPrint = "C: "
for i in ProfileMatrix.Cstr:
    CPrint += str(i) + " "
print(CPrint)
GPrint = "G: "
for i in ProfileMatrix.Gstr:
    GPrint += str(i) + " "
print(GPrint)
TPrint = "T: "
for i in ProfileMatrix.Tstr:
    TPrint += str(i) + " "
print(TPrint)