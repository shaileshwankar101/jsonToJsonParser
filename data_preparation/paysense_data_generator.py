import json
import random
from faker import Faker

fake = Faker()
statuses = ["Disbursal", "Docs Verified", "Courier", "Credit Ops", "NMI", "App Pending", "App Submit",
            "Credit Approved"]


def generate_paysense_data(id):
    return {
        "master_id" : f"CU_{random.randint(9000000000, 9999999999)}",
        "first_name" : fake.first_name(),
        "last_name" : fake.last_name(),
        "email" : fake.email(),
        "state" : fake.state(),
        "estimated_salary" : random.randint(40000, 90000),
        "loan_id" : f"L{random.randint(100, 999)}",
        "loan_required_amount": random.randint(5000, 20000),
        "loan_approved_amount": random.randint(4000, 18000),
        "approved_emi": random.randint(1000, 3000),
        "loan_tenure": random.randint(6, 24),
        "status": random.choice(statuses),
        "current_priority": f"P{random.randint(1, 3)}"
    }


def save_to_json(data, file_name):
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=2)


def generate_and_save_data():
    for i in range(10):
        master_id = i
        paysense_data = generate_paysense_data(master_id)
        file_name = f'paysense_data_{master_id}.json'
        save_to_json(paysense_data, file_name)


generate_and_save_data()
