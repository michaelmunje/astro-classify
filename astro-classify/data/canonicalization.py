from os import listdir
import sys

if len(sys.argv) == 1 or len(sys.argv) > 3:
    print('Expects an argument of the folder containing the data files')
    print('Can also take a second optional parameter of where the master file should be created')
else:
    path = sys.argv[1]
    files = listdir(path)
    values = set()

    for file in files:
        file_data = open(path + '\\' + file, 'r');
        for line in file_data:
            if line.strip().strip('\n') != '':
                value = line.strip('\n')
                values.add(value)
    outputFile = 'Master.txt'
    if(len(sys.argv) == 3):
        outputFile = sys.argv[2] + '\\' + outputFile
    writeFile = open(outputFile, 'w')
    for value in values:
        writeFile.write(value + '\n')
    print('New file created, ' + outputFile)