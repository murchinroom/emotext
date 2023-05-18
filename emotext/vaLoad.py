import csv

f = open('data/情感词汇-VAspace.csv', 'r')
spamreader=csv.DictReader(f)
dict = {}
for row in spamreader:
    # print(row)
    dict[row['class']] = [float(row['valance']),float(row['arouse'])]
print(dict)