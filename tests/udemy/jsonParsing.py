import json

# Read JSON from string
courses = '{"name": "test automation","languages": ["Java","Python"]}'
dict_courses = json.loads(courses)
# print(type(dict_courses))

# Read JSon from file
with open('F:/TAU/Python3Demo/json_file.json') as f1:
    dict_data1 = json.load(f1)
    # print(type(dict_data["courses"]))
    for course in dict_data1["courses"]:
        # print(course)
        # print(type(course))
        # print(course["title"])
        if course["title"] == "Cypress":
            print(course["price"])
            # assert course["price"] == 67

with open('F:/TAU/Python3Demo/json_file_copy_edited.json') as f2:
    dict_data2 = json.load(f2)
    assert dict_data1 == dict_data2
