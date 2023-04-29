import json
data = json.load(open('../code.json'))

input_dict = {"memberOrgs": [], "orgs": [], "repos": []}

array_for_objects = []
for item in data:
    if item['name'] == ".github":
        continue
    array_for_objects.append(item['full_name'])
input_dict["repos"] = array_for_objects

#### save and overwrite
# input_lists_f = open(path_to_input_lists_json, "w")
# appended_input_lists_string_dumped = json.dumps(appended_input_lists_string)
path_to_input_lists_json = "../input_lists.json"
with open(path_to_input_lists_json, 'w') as file:
    json.dump(input_dict, file)