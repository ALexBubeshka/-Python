import json

results = {}
def searching_el(msg):
    global results
    with open('employees.json', 'r') as file:
        data = json.load(file)

        for k, v in data.items():
            for i in range(len(msg)):
                if v['Full name'] == msg:
                    results[k] = v
                elif v['Sex'] == msg:
                    results[k] = v
                elif v['Birth date'] == msg:
                    results[k] = v
                elif v['Marital status'] == msg:
                    results[k] = v
                elif v['Job title'] == msg:
                    results[k] = v
                elif str(v['salary']) == msg:
                    results[k] = v
                elif str(v['Phone numbers'][0]) == msg:
                    results[k] = v
                elif str(v['Phone numbers'][1]) == msg:
                    results[k] = v
    print(results)