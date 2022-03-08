import json

def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def write_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

a = {"a": "c"}
data = read_json('Test/data.json')
data['planets'].append(a)

write_json('Test/data.json', data)