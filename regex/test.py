import re

line = "cats 2are smar3ter than dogs1 caaaats "
p = re.compile('[a-z]+')
m = p.match("temp asdf")
print m.group()
