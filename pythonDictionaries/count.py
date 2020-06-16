# The following python program utilizes dictionaries to count and keep track of different words in a txt file
# and then prints the most occuring word, and the number of times it appears. 

name = input('Enter the files name: ')
handle = open(name)

counts= dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]= counts.get(word, 0) +1

# At this point, the program has counted all words, and there is a virtaul histogram

bigcount= None
bigWord = None

for word, count in counts.items():
    if bigcount is None or count>bigcount:
        bigWord= word
        bigcount = count

print(bigWord, bigcount)

# Exanple run- Entering words.txt outputs "to 16" meaning "to" is the most occuring word at a count of 16