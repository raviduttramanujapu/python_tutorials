'''
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
'''


def exception_sample(x, y):
  try:
    print 'First statement'
    return str(x / float(y))
    print 'No error'
  except ZeroDivisionError:
    print 'Zero Division error happened'
    return 'inf'
  finally:
    print 'Final block got executed'
    return '100'

print exception_sample(10, 0)



def x(y):
  if (y==5):
    return 'true'
  if (y==5):
    return 'true true'
#print x(5)