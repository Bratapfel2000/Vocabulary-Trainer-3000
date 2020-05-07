import csv

##vocabulary_file = 'vokabeln_short.csv'

#csv file reader, returns tuple
def readMyFile(filename):
    lang1 = []
    lang2 = []
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            lang1.append(row[0])
            lang2.append(row[1])
    return lang1, lang2

#csv file reader, returns tuple
def readMyFile_four_columns(filename):
    lang1 = []
    lang2 = []
    val1 = []
    val2 = []
    val3 = []
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            lang1.append(row[0])
            lang2.append(row[1])
            val1.append(row[2])
            val2.append(row[3])
##            val3.append(row[4])
    return lang1, lang2, val1, val2#, val3



#takes tuple from readmyfile and makes dict 
def fields(filename):
    field = {}
    lang1,lang2 = readMyFile(filename)
    for i in range(len(lang1)):
        field[i] = [0,0]
        field[i][0] = lang1[i]
        field[i][1] = lang2[i]
    return field

#same like fields() but with extra '0' for saving right/wrong
def fields_w_vals(filename):
    field = {}
    lang1,lang2 = readMyFile(filename)
    for i in range(len(lang1)):
        field[i] = [0,0,0,0]
        field[i][0] = lang1[i]
        field[i][1] = lang2[i]
    return field


#same like fields() but with extra '0' for saving right/wrong
def fields_w_four_vals(filename):
    field = {}
    lang1,lang2,val1,val2 = readMyFile_four_columns(filename)
    for i in range(len(lang1)):
        field[i] = [0,0,0,0]
        field[i][0] = lang1[i]
        field[i][1] = lang2[i]
        field[i][2] = val1[i]
        field[i][3] = val2[i]      
    return field

#same like fields() but with extra '0' for saving right/wrong
def fields_w_five_vals(filename):
    field = {}
    lang1,lang2,val1,val2 = readMyFile_four_columns(filename)
    for i in range(len(lang1)):
        field[i] = [0,0,0,0,0]
        field[i][0] = lang1[i]
        field[i][1] = lang2[i]
        field[i][2] = val1[i]
        field[i][3] = val2[i]      
    return field


#menu item: 'Export csv file'
def csv_exporter(vocabulary_dictionary,file_namer):
##    file_namer = input("enter name for csv-file or [Enter] to go back: ")
    if file_namer == "":
        return 
    else:
       with open(file_namer+'.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in vocabulary_dictionary.items():
           writer.writerow([key, value[0], value[1], value[2], value[3]])
        print(" ")
        print('"'+file_namer+'.csv'+'"'+" exported")
##        print(" ")
##        input("Press [Enter] to go back")
        return

#menu item: 'Export csv file'
def csv_exporter_2(vocabulary_dictionary,file_namer):
##    file_namer = input("enter name for csv-file or [Enter] to go back: ")
    if file_namer == "":
        return 
    else:
       with open(file_namer+'.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in vocabulary_dictionary.items():
           writer.writerow([key, value[0], value[1], value[2], value[3]])
        print(" ")
        print('"'+file_namer+'.csv'+'"'+" exported")
##        print(" ")
##        input("Press [Enter] to go back")
        return

#trying to wipe out the additional number at [0]-position
def csv_exporter_3(vocabulary_dictionary,file_namer):
    if file_namer == "":
        return 
    else:
       with open(file_namer+'.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in vocabulary_dictionary.items():
           writer.writerow([value[0], value[1], value[2], value[3]])
        print(" ")
        print('"'+file_namer+'.csv'+'"'+" exported")

        return
