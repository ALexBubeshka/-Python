import json

def del_el(exempl_1):
    global del_element
    with open('employees.json', 'r') as file:
        data = json.load(file)
        for k, v in data.items():
            if v['Full name'] == exempl_1:
                del data[k]
                break
    with open('employees.json', 'w')as file:
        json.dump(data, file, indent=4)




