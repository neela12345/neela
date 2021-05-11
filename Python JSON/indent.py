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
print(json.dumps(x,indent=3))
