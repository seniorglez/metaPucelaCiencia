import os
import json

unique_user_ids = set()

json_files = [file for file in os.listdir('./transformationA') if file.endswith('.json')]

for file_name in json_files:
    with open(f'./transformationA/{file_name}', 'r') as input_file:
        data = json.load(input_file)

    user_ids = set(data.get('users', []))
    room_admin_ids = set(data.get('roomAdmins', []))

    unique_user_ids.update(user_ids - room_admin_ids)

unique_user_count = len(unique_user_ids)

print(f'Total unique user IDs: {unique_user_count}')