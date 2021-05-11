import json
x={
"name":"neela",
"age":19,
"city":"tuty",
"married":False,
"pets":"cat",
"cars":[
    {"model":"bmw"},
    {"model":"ford"}
    ]
}
y=json.dumps(x)
print(y)
