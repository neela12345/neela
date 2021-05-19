import re
txt='the rain in spain'
x=re.findall('\s',txt)
print(x)
if x:
    print('yes they match')
else:
    print('no match')
