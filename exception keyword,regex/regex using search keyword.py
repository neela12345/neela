import re
txt='the rain in spain'
x=re.search('^the.*spain$',txt)
if x:
    print('yes they match')
else:
    print('no match')
