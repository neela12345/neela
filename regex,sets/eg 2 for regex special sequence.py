import re
txt='the rain in spain for 3 days'
x=re.findall('\d',txt)
print(x)
if x:
    print('yes they match')
else:
    print('no match')
