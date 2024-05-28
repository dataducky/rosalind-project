import re
#initalize values
GCdict = {}
count, lineCount, lineTotal = 0, 0, 0
match = r'^>'
strID = ""
strand = ""
#counts total lines for last entry to be printed
with open(r"5inputfile.txt", 'r') as totaler:
    lineTotal = len(totaler.readlines())

GCinput = open('5inputfile.txt','r')
for line in GCinput:
    lineCount += 1
    if re.match(match, line):
        # GC % calculator, saves to dict assigned to strID
        if strand != "":
            GCPercentage = 0.0
            GCcount, total = 0, 0
            for i in strand.strip():
                if i == "G" or i == "C":
                    GCcount += 1
                total += 1
            GCPercentage = GCcount / total
            GCdict[strID] = GCPercentage

        #initializes strand ID to save to dict
        strID = line[1:].strip() 
        
        # ending sequence 
        count += 1
        strand = ""
    else:
        strand += line.strip()
    if lineCount == lineTotal:
        GCPercentage = 0.0
        GCcount, total = 0, 0
        for i in strand:
            if i == "G" or i == "C":
                GCcount += 1
            total += 1
        GCPercentage = GCcount / total
        GCdict[strID] = GCPercentage
GCinput.close()

#highest value-ator
highestValue, highestKey = 0.0, ""
for key, value in GCdict.items():
    if value >= highestValue:
        highestValue = value
        highestKey = key
print (highestKey)
print (highestValue * 100)
