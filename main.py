import json

data = {'Hello': 'World!', 'Status': 'Init', 'active': True}

# write to a JSON file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)  # pretty print

# read from a JSON file
with open('data.json', 'r') as f:
    data = json.load(f)

print(data)