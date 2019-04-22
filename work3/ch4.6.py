mySent = 'This book is the best book on Python or M.L I have ver laid eyes upon.'
# print(mySent.split())

import re
regEx = re.compile('\\W+')
listOfTokens = regEx.split(mySent)
print(listOfTokens)

import sys
print(sys.version)