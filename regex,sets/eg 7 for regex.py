import re
txt='the rainsss in spain'
x=re.findall('ins+',txt)
print(x)
if x:
    print('yes they match')
else:
    print('no match')
