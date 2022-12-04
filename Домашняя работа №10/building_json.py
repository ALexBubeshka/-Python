from db import employees
import json

def building_first_json():
    with open('employees.json', 'w') as db:
        json.dump(employees, db, indent=4)


building_first_json()