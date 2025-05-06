# JASON - An attempt to learn how to use JSON in Python

## What is JSON?

JSON is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate. It is based on a subset of the JavaScript Programming Language, Standard ECMA-262 3rd Edition - December 1999.

JSON is a text format that is completely language independent but uses conventions that are familiar to programmers of the C-family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others. These properties make JSON an ideal data-interchange language.

JSON is built on two structures:

- A collection of name/value pairs. In various languages, this is realized as an object, record, struct, dictionary, hash table, keyed list, or associative array.
- An ordered list of values. In most languages, this is realized as an array, vector, list, or sequence.

## Why JSON?

JSON is easy for humans to generate and parse, but less easy for machines to generate and parse.

## How to use JSON in Python

### Reading JSON

```python
import json

with open('data.json', 'r') as f:
    data = json.load(f)

print(data)
```

### Writing JSON

```python
import json

data = {'Hello': 'World!', 'Status': 'Init', 'active': True}

# write to a JSON file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)  # pretty print
```

### JSON to Python

```python
import json

data = {'Hello': 'World!', 'Status': 'Init', 'active': True}

# write to a JSON file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)  # pretty print

with open('data.json', 'r') as f:
    data = json.load(f)

print(data)
```

### JSON to Python

```python
import json

data = {'Hello': 'World!', 'Status': 'Init', 'active': True}

# write to a JSON file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)  # pretty print

with open('data.json', 'r') as f:
    data = json.load(f)

print(data)
```

## Resources

- [JSON](https://www.json.org/)
- [JSON in Python](https://docs.python.org/3/library/json.html)
- [JSON in Python - Tutorial](https://www.w3schools.com/python/python_json.asp)
- [JSON in Python - Tutorial - JSON to Python](https://www.w3schools.com/python/python_json_convert.asp)
