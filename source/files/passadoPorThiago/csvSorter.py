import math
import csv

log = []

with open('3_log.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    i=0
    j=0
    anterior = -1
    for line in csv_reader:
        log.append([])
        for collum in line:
            log[i].append(collum)
            j += 1
        i += 1
        anterior = line[0] 



#print(log)
