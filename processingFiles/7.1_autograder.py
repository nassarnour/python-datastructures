#7.1 Write a program that prompts for a file name, then opens that file and reads 
# through the file, and print the contents of the file in upper case. Use the file words.txt to 
# produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt

fname= input('Enter file name: ')
try:
    fileHandler=open(fname)

    numOfRows = 0
    totalAmount=0
    tempValue=0
    average=0

    for line in fileHandler:
        line=line.rstrip()
        if line.startswith("X-DSPAM-Confidence:"):
            tempValue=(line[20:28]) #gets current number
            totalAmount= float(totalAmount)+float(tempValue) #adds it to total
            numOfRows= numOfRows+1 #count total
            #divide by total
    average=float(totalAmount)/float(numOfRows)
    
    print('Average spam confidence:', average)
except:
    print('Could not open: ',fname)
    quit()