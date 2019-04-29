import csv
file = open("test.txt","w")
with open("train.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    print("reached")
    data = []
    for row in csv_reader:
        if row[2] == "1":
            file.write(row[1])
file.close()
file2 = open("test2.txt","w")
with open("train.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    print("reached")
    data = []
    for row in csv_reader:
        if row[2] != "1":
            file2.write(row[1])
file2.close()
