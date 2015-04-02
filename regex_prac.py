import re

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r'''
    ^([-\w\s]+),\s
    ([-\w\s]+):
    (\d)$
''', string, re.X|re.M)