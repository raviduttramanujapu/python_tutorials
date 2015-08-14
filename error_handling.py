def divi (i, j):
    return i / float(j)

print divi (9, 2)
try:
    print div(3, 0)
    print 'here'
except ZeroDivisionError:
    print 'except block is getting executed'
    print divi(4, 6)

print divi (4, 6)
