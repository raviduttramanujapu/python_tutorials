import csv

file = open('odi-batting.csv', 'r')

data = csv.DictReader(file)



'''
Script to get the number of lines
'''
count_lines = 0
for line in data:
    count_lines = count_lines + 1

# print 'No. of lines = ' + str(count_lines)

file.seek(0)


'''
Get the unique countries
'''
countries = []
'''
for line in data:
    if line['Country'] != 'Country':    
      curr_country = line['Country']
      if curr_country not in countries:
          countries.append(curr_country)
# print countries

'''



'''
result = {}
file.seek(0)
for line in data:
  if line['Country'] != 'Country':
      curr_country = line['Country']
      if curr_country in result:
          result[curr_country] = result[curr_country] + 1
      else:
          result[curr_country] = 1

print result
'''


'''
Countrywise Total Runs
'''


'''
result = {}
file.seek(0)
for line in data:
  #line['Runs'] = line['Runs'].replace('', 'nan')
  if line['Country'] != 'Country':
      curr_country = line['Country']
      if curr_country in result:
          result[curr_country] = result[curr_country] + int(line['Runs'])
      else:
          result[curr_country] = int(line['Runs'])

print result
'''


'''
Converting in to a function
'''

def calc_total(line, result, col_name, metric_name, year):
  if line[col_name] != col_name:
      curr_country = line[col_name]
      if curr_country in result:
          result[curr_country] = result[curr_country] + float(line[metric_name])
      else:
          result[curr_country] = float(line[metric_name])
  return



result = {}
col_name = 'Country'
metric_name = 'ScoreRate'
year = '2010'
file.seek(0)
for line in data:
  calc_total(line, result, col_name, metric_name, year)
  #line['Runs'] = line['Runs'].replace('', 'nan')


print result



