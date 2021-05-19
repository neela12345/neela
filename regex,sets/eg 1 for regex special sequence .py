import re
txt='hai neela'
x=re.findall('\Ahai',txt)
print(x)
if x:
    print('yes they match')
else:
    print('no match')
