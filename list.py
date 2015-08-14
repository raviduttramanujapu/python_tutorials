data1 = [10, 20, 40, 2, 7]
data2 = [10, 5, 6, 8, 2]

# Check for common elements between two lists
'''
result = []
for i in range(len(data1)):
    curr_elem = data1[i]
    if curr_elem in data2:
        result.append(curr_elem)
print result
'''

# Check for both index and element
'''
result = []
for i in range(len(data1)):
    if data1[i] == data2[i]:
        result.append(data1[i])
print result
'''

'''
# Reverse the list without any inbuilt function
data = [10, 20, 40, 2, 7]
result = [0] * len(data)
n = len(data)
for i in range(n):
    result[n - i -1] = data[i]
print result
'''

data = range(10)
'''
print '==========INPUT==========='
print data
result = []
n = len(data)
print n
for i in range(n):
    print i, result
    result.append(data[i] * data[i])
print '==========OUTPUT=========='
print result
'''

data1 = [10, 20, 40, 2, 7]

d = {'a': 1, 'b': 2}
print d