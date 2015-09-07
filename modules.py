'''
import ip_utilities as ip
# from ip_utilities import validate_ip
# from ip_utilities import validate_ip, is_string
# from ip_utilities import *

if ip.validate_ip('216.58.196.110'):
  print 'Valid ip'
else:
  print 'Not valid'


if ip.is_string('216.58.196.110'):
  print 'Valid ip'
else:
  print 'Not valid'
'''

def sq_num(num):
  print num * num
  return num * num

def triple_num(num):
  print sq_num(num) * num


if __name__ == '__main__':
  path = '/data/data.csv'
  sq_num(path)
  print 'This is a source file'
  triple_num(4)