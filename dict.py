data = {'a': 1, 'b': 2}

'''
for key in data:
    print  # Get the key
    print data[key] # Gets the value for that key
'''


'''
for key, val in data.iteritems():
    print 'Key: ' + key +  ', Value: ' + str(val)
'''

'''
for key in data.iteritems():
    print key
'''


'''
data = {'a': 1, 'b': 2, 'c': 3}
print data
for key, val in data.iteritems():
    print key, val
    data[key] = data[key] * data[key]
print data

result = {}
for key, val in data.iteritems():
    result[val] = key
print data
print result
'''

data = {'kathir': ['mani', 'sukumar'], 'pavan': ['kumar']}
print data

for key, val in data.iteritems():
  for name in val:
    print key
    print name
  print '---------------'