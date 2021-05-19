import re
txt='The rain in Spain for 30 days'
x=re.findall('[a-zA-Z]',txt)
print(x)
if x:
    print('yes they match')
else:
    print('no match')
