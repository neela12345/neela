import re
txt='the rain in spain for 3_days'
x=re.findall('\w',txt)
print(x)
if x:
    print('yes they match')
else:
    print('no match')
