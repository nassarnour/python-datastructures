#8.4 Open the file romeo.txt and read it line by line. 
#For each line, split the line into a list of words using the split() method. 
#The program should build a list of words. 
#For each word on each line check to see if the word is already in the list and if not append it to the list. 
#When the program completes, sort and print the resulting words in alphabetical order#

fname = input("Enter file name: ")

fh = open(fname)
lst = list()

for line in fh:
    tempVariable=0
    line.rstrip()
    tempLine=line.split()
    tempSize=len(tempLine)

    for group in tempLine:
        if(tempVariable!=tempSize):
            tempWord= tempLine[tempVariable]
            tempVariable=tempVariable+1
            if(len(lst)==0):
                lst.append(tempWord)
            for individual in lst:
                if(lst.count(tempWord)>=1):
                    break
                else:
                    lst.append(tempWord)
sortedList=sorted(lst)
print(sortedList)

