import re
#initalize values
DNAdict = {}
count, lineCount, lineTotal = 0, 0, 0
match = r'^>'
strID = ""
strand = ""
#counts total lines
with open(r"14inputfile.txt", 'r') as totaler:
    lineTotal = len(totaler.readlines())

#Opens the input file and scans each line. Saves FASTA format text files into a dictionary(DNAdict)
GCinput = open('14inputfile.txt','r')
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



def isReversePalindrome(inputStrand):
    ReverseCompliment = ""
    inputLength = len(inputStrand) - 1
    ctr = 0
    for i in range(inputLength + 1):
        nuc = inputStrand[(inputLength - ctr)]
        if nuc == "A":
            ReverseCompliment += "T"
        if nuc == "C":
            ReverseCompliment += "G"
        if nuc == "G":
            ReverseCompliment += "C"
        if nuc == "T":
            ReverseCompliment += "A"
        ctr += 1
    #print(inputStrand)
    #print(len(inputStrand))
    #print(ReverseCompliment)
    #print(len(ReverseCompliment))
    startingLength = 3
    
    for i in range(9):
        if i % 2 == 1:
            continue
        lengthMod = startingLength + i + 1
        ctr = 0
        for j in inputStrand:
            if (ctr+lengthMod) > len(inputStrand):
                continue
            #print(DNAstr[ctr:(ctr+lengthMod)])
            findStr = inputStrand[ctr:(ctr+lengthMod)]
            findResult = ReverseCompliment.find(findStr)
            revStr = ReverseCompliment[(inputLength-ctr-lengthMod+1):(inputLength-ctr+1)]
            if findResult != -1:
                if findStr == revStr:
                    #print("Happy")
                    #print(str(ctr+1) + ", " + str(i+4) +", " +findStr)
                    print(str(ctr+1) + " " + str(i+4))
                

            ctr += 1


for i in DNAdict:
    isReversePalindrome(DNAdict[i])


