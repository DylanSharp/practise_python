import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w\s]+))\t  # Last and First Names
    (?P<email>[-\w\d.*+]+@[-\w\d.]+)\t  # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # Phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?  # Job and Company
    (?P<twitter>@[\w\d]+)?$  # Twitter
''', re.X|re.M)

for match in line.finditer(data):
    print("{first} {last} \n\tEmail: {email}".format(**match.groupdict()))