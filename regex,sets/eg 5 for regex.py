import re
txt='hai neela'
x=re.findall('neela$',txt)
if x:
    print('yes they match')
else:
    print('no match')
