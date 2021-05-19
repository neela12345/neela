import re
txt='hai neela'
x=re.findall('^hai',txt)
if x:
    print('yes they match')
else:
    print('no match')
