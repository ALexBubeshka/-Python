import json

data = ''
def reading_json():
    global data
    with open('employees.json', 'r') as file:
        data = json.load(file)
        for k, v in data.items():
            print(k, v)
    with open('employees.json', 'w')as f:
        json.dump(data, f, indent=4)

reading_json()
