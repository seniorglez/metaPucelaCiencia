import os
import json
import shutil

in_dir='./raw'
out_dir='./transformationA'
desired_fields = [
    'id',
    'ownerID',
    'owner',
    'timeLastJoined',
    'activeParticipants',
    'roomAdmins',
    'createdAt',
    'users',
    'activeParticipantCount',
    'likes',
    'views',
    'isInstanceable',
    'likedSpace',
    'promoted',
    'lastPromoted'
    ]

if os.path.exists(out_dir):
    shutil.rmtree(out_dir)

os.makedirs(out_dir)

json_files = [file for file in os.listdir(in_dir) if file.endswith('.json')]

for file_name in json_files:
    with open(f'./raw/{file_name}', 'r') as input_file:
        data = json.load(input_file)

    first_room = data['rooms'][0]
    filtered_first_room = {field: first_room[field] for field in desired_fields}

    with open(f'{out_dir}/{file_name}', 'w') as output_file:
        json.dump(filtered_first_room, output_file, indent=4)
