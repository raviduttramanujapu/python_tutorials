import csv

file = open('sample.csv', 'r')

data = csv.DictReader(file)

'''
# Year-wise total runs

result = {}
for row in data:
  if row['Country'] != 'Country':
    curr_year = row['MatchDate'][-4:]
    if curr_year not in result:
      result[curr_year] = int(row['Runs'])
    else:
      result[curr_year] = result[curr_year] + int(row['Runs'])

print result
    
for year, runs in result.iteritems():
  print year, runs
'''

'''
file.seek(0)
result = {}
for row in data:
  if row['Country'] != 'Country':
    try:
      curr_year = row['MatchDate'].split('/')[0]
    except IndexError:
      curr_year = row['MatchDate'].split('-')[0]
    print curr_year
    if curr_year not in result:
      result[curr_year] = int(row['Runs'])
    else:
      result[curr_year] = result[curr_year] + int(row['Runs'])

print result
for month, runs in result.iteritems():
  print month, runs
'''




'''
result = {}
import datetime
for row in data:
  if row['Country'] != 'Country':
    curr_year = datetime.datetime.strptime(row['MatchDate'], '%d/%m/%Y')
    curr_year = curr_year.day
    if curr_year not in result:
      result[curr_year] = int(row['Runs'])
    else:
      result[curr_year] = result[curr_year] + int(row['Runs'])

for month, runs in result.iteritems():
  print month, runs

'''


file.seek(0)
import numpy as np
result = {}
for row in data:
  if row["Country"] != 'Country':
    if row['Player'] not in result:
      result[row['Player']] = [int(row['Runs'])]
    else:
      result[row['Player']].append(int(row['Runs']))


for player, runs in result.iteritems():
  print player, np.average(runs)

