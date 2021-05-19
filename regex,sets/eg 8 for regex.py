import re
txt='the rain in spain falls mainly in the plain'
x=re.findall('al{2}',txt)
print(x)
if x:
    print('yes they match')
else:
    print('no match')
