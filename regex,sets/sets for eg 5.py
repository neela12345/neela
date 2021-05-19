import re
txt='the rain in spain for 30 days'
x=re.findall('[0-5][0-9]',txt)
print(x)
if x:
    print('yes they match')
else:
    print('no match')
