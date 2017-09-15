import os

# enter file input name
mentionMap = 'lastMentionMap.txt'

# get Current path of this file
currentPath = os.getcwd()

# Start reading the file in separate lines
with open(currentPath + '/' + mentionMap) as f:
    lines = f.readlines()
    # stripping the newline character
    lines = [x.strip() for x in lines]

finalList = []

#now let's create two lists with the doc names and references separately
docList = []
referenceList = []

for newLine in lines:
    docList.append(newLine.split(';')[0])
    referenceList.append(newLine.split(';')[1])

count = 0
for document in docList:
    print(str(count+1) + '/' + str(len(docList)))
    for reference in referenceList[count].split(','):
        finalList.append(document + ' ' + reference)

    count = count+1

# create new file to add non empty entries
finalFile = open('finalEdgelist.edgelist', 'w')

for finalLine in finalList:
    print(finalLine, file=finalFile)
finalFile.close()