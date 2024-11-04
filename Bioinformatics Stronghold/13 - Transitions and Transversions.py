import re
#initalize values
DNAdict = {}
count, lineCount, lineTotal = 0, 0, 0
match = r'^>'
strID = ""
strand = ""
#counts total lines
with open(r"13inputfile.txt", 'r') as totaler:
    lineTotal = len(totaler.readlines())

#Opens the input file and scans each line. Saves FASTA format text files into a dictionary(DNAdict)
GCinput = open('13inputfile.txt','r')
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

ctr, transitionCtr, transversionCtr = 0,0,0
for key in DNAdict:
    if ctr > 0:
        secondKey = key
        break
    firstKey = key
    ctr += 1

ctr = 0
for i in DNAdict[firstKey]:
    if i == DNAdict[secondKey][ctr]:
        ctr += 1
        continue
    if i == "A" or i == "G":
        if DNAdict[secondKey][ctr] == "A" or DNAdict[secondKey][ctr] == "G":
            transitionCtr += 1
        else:
            transversionCtr += 1
    if i == "T" or i == "C":
        if DNAdict[secondKey][ctr] == "T" or DNAdict[secondKey][ctr] == "C":
            transitionCtr += 1
        else:
            transversionCtr += 1
    ctr += 1

ratio = transitionCtr/transversionCtr
print(round(ratio,11))
