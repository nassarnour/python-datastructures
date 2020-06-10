
#Assigment Directions in the txt file 

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
herecount=0
countBlanks = 0

lst=list()

seekColon='From:'
seek='From'

for line in fh:
    line.rstrip()
    tempLine=line.split()
    herecount=herecount+1

    if len(tempLine)==0:
        countBlanks = countBlanks+1

    else:
        if tempLine[0]==seekColon:
            storeEmail=tempLine[1]
            count=count+1
            lst.append(storeEmail)

for x in range(len(lst)): 
    print(lst[x])
print("There were", count, "lines in the file with From as the first word")