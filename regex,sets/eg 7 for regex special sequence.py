import re
txt='the rain in spain'
x=re.findall('\W',txt)
print(x)
if x:
    print('yes they match')
else:
    print('no match')
