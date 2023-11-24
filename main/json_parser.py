import json
import os
paysense_data_directory = os.path.abspath('../data_preparation')
zendesk_data_directory = os.path.abspath('../data_generation')


def transform_to_zendesk_format(paysense_data):
    zendesk_data = {
        "zendesk_ticket": {
            "id": paysense_data["master_id"],
            "requester": {
                "first_name": paysense_data["first_name"],
                "last_name":paysense_data["last_name"],
                "email": paysense_data["email"]
            },
            "location": {
                "state": paysense_data["state"],
                "county": paysense_data["estimated_salary"]
            },
            "loan_details": {
                "loan_id": paysense_data["loan_id"],
                "loan_required_amount": paysense_data["loan_required_amount"],
                "loan_approved_amount": paysense_data["loan_approved_amount"],
                "approved_emi": paysense_data["approved_emi"],
                "loan_tenure": paysense_data["loan_tenure"]
            },
            "ticket_status": {
                "status": paysense_data["status"],
                "priority": paysense_data["current_priority"]
            }
        }
    }
    return zendesk_data


def save_to_json(data, file_name):
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=2)


for filename in os.listdir(paysense_data_directory):
    if filename.startswith("paysense_data_") and filename.endswith(".json"):
        paysense_file_path = os.path.join(paysense_data_directory, filename)

        with open(paysense_file_path, 'r') as paysense_file:
            paysense_data = json.load(paysense_file)

        zendesk_data = transform_to_zendesk_format(paysense_data)

        zendesk_file_path = os.path.join(zendesk_data_directory, f'zendesk_file_transformed_{filename}')
        save_to_json(zendesk_data, zendesk_file_path)





