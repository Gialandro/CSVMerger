import csv
import math
import os
import time

asciimoji = ('ᕦ( ͡° ͜ʖ ͡°)ᕤ', '╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ', '(╯°□°)╯︵ ┻━┻', 'ヽ(｀Д´)ﾉ')
os.system('cls||clear')
print('PyMerge Alpha0.1')
print("WARNING! Both files MUST have same number of rows to create merged CSV correctly {0}".format(asciimoji[3]))
# File 1
while True:
    try:
        csvLocation1 = str(input('Enter the name of first CSV to open like "file.csv": '))
        csv1 = open(csvLocation1, newline = '', encoding='utf-8')
        read1 = list(csv.reader(csv1))
        break
    except IOError:
        print('File not found, try again. {0}'.format(asciimoji[2]))
    except ValueError:
        print('Invalid number of rows, try again. {0}'.format(asciimoji[3]))
# File 2
while True:
    try:
        csvLocation2 = str(input('Enter the name of second CSV to open like "file.csv": '))
        csv2 = open(csvLocation2, newline = '', encoding='utf-8')
        csv2.__next__() #Header deleted
        read2 = list(csv.reader(csv2))
        break
    except IOError:
        print('File not found, try again. {0}'.format(asciimoji[2]))
    except ValueError:
        print('Invalid number of rows, try again. {0}'.format(asciimoji[3]))

nameCSV = 'MergedCSV'
newList = read1 #List without repeted elements
for row in read2:
    if row not in read1:
        newList.append(row)

os.system('cls||clear')
print('Creating CSV... {}'.format(asciimoji[0]))
time.sleep(2)
with open('MergedCSV.csv', 'w') as fileCSV:
    fileWriter = csv.writer(fileCSV, quoting = csv.QUOTE_ALL, lineterminator='\n')
    fileWriter.writerows(newList)
os.system('cls||clear')
print('Done! {}'.format(asciimoji[1]))
# Closing CSVs
csv1.close()
csv2.close()
# newCSV = open('/Users/ctconsulting7/Documents/PythonScripts/PyCSVs/PyMerge/newCSV.csv', 'w', encoding='utf-8')
# writer = csv.writer(newCSV, lineterminator='\n')
# writer.writerows(newList)
