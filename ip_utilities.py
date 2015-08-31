import urllib2

def is_string(address):
  return True if type(address) == str else False

def validate_ip(address):
  try:
    webpage = urllib2.urlopen('http://' + address)
    return True
  except urllib2.URLError:
    return False


