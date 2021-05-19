import re
x='how are you,how is everything'
x=re.match('how',x)
print(x.span())
print(x.group())
print(x.string())
