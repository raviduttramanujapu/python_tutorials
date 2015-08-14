import csv

file = open('odi-batting.csv', 'r')
data = csv.reader(file)

'''
data2 = csv.reader(file)

countries = []
for i, line in enumerate(data1):
    if i != 0:
      if line[0] not in countries:
        countries.append(line[0])


result = {}
for country in countries:
    counter = 0
    for line in data2:
        print counter
        if line[0] == country:
            counter = counter + 1
    result[country] = counter
print result

'''


result = {}

for line in data:
    country = line[0]
    if country in result:
        result[country] = result[country] + 1
    else:
        result[country] = 1
print result