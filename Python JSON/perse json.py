import json
x='{"name":"neela","age":19,"city":"tuty"}'
y=json.loads(x)
print(y["name"])
print(y["age"])
print(y["city"])
