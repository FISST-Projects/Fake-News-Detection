import csv
reader = csv.reader(open("Op_India_Dataset.csv", encoding="utf8"))
reader1 = csv.reader(open("OpIndia_Dataset.csv", encoding="utf8"))
reader2 = csv.reader(open("India_Today_Dataset.csv", encoding="utf8"))
reader3 = csv.reader(open("FactCheckDataset.csv", encoding="utf8"))


f = open("dataset.csv", "w", encoding="utf8")
writer = csv.writer(f)

for row in reader:
    writer.writerow(row)
for row in reader1:
    writer.writerow(row)
for row in reader2:
    writer.writerow(row)
for row in reader3:
    writer.writerow(row)

f.close()

with open('dataset.csv', "r", encoding="utf8") as input, open('Fake_News_Dataset.csv', 'w', encoding="utf8") as output:
    non_blank = (line for line in input if line.strip())
    output.writelines(non_blank)
