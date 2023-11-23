import json

data = {'name': 'Soham Wadekar', 'age': 18, 'city': 'Pune'}

with open('intermediates/file handling/files/test.json','w') as f:
    print("Dumping data into file...")
    json.dump(data,f)
    print("Done!")

with open('intermediates/file handling/files/test.json','r') as f:
    print("Retrieving data from file...")
    loaded_data = json.load(f)
    print(loaded_data)