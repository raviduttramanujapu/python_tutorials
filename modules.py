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