import sys

args = sys.argv

data = args[1].split(',')
oper = args[2]

print data
print oper

result = 0
if oper == 'add':
    for i in data:
        result = result + float(i)
elif oper == 'sub':
    for i in data:
        result = result - float(i)
elif oper == 'mul':
    result = 1
    for i in data:
        result = result * float(i)
else:
    print 'Give only add, sub or mul as input'
print result