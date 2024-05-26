counter = 0
output = open('5outputfile.txt', 'w')
with open('5inputfile.txt', 'r') as f:
    for i in f:
        counter += 1
        if counter % 2 == 0:
            output.write(i)
output.close()
output = open('5outputfile.txt', 'r')
for line in output:
    print(line.strip())