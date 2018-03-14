import csv
# File 1
file1 = open('/Users/ctconsulting7/Documents/PythonScripts/PyCSVs/PyMerge/csv1.csv', newline = '', encoding='utf-8')
reader1 = csv.reader(file1)
lstRead1 = list(reader1)

# File 2
file2 = open('/Users/ctconsulting7/Documents/PythonScripts/PyCSVs/PyMerge/csv2.csv', newline = '', encoding='utf-8')
file2.__next__() #Delete header python3
reader2 = csv.reader(file2)
lstRead2 = list(reader2)

newList = lstRead1 #List without repeted elements
for row in lstRead2:
    if row not in lstRead1:
        newList.append(row)
for lin in newList:
    print(lin)

newCSV = open('/Users/ctconsulting7/Documents/PythonScripts/PyCSVs/PyMerge/newCSV.csv', 'w', encoding='utf-8')
writer = csv.writer(newCSV, lineterminator='\n')
writer.writerows(newList)
