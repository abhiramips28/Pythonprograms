""" json - sorting & exchanging data"""
'''dumps -> python to json convert'''
import json
x = {"name":"anvi","age":3}
print(type(x))
y = json.dumps(x)
print(y)
print(type(y))


'''loads -> json to python convert'''
x = '{"name":"anvi","age":3}'
print(type(x))
y = json.loads(x)
print(y)
print(type(y))