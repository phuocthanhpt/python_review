import requests
import random
import json
import string

# base_url
base_url = "https://gorest.co.in"

# Auth_token
auth_token = "Bearer 9801659f47e16445d081dd5d47c3ac5356447a475bb20acced6aab10e6f943e5"
headers = {
    "Authorization": auth_token
}


def generate_random_name():
    N = 7  # number of characters
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
    return random_string


def generate_random_email():
    N = 10  # number of characters
    domain = "email.com"
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
    random_email = random_string + "@" + domain
    return random_email


# Get Request
def get_request():
    url = base_url + "/public/v2/users/"
    print("Get url: ", url)
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_response = response.json()
    print("1111111111: ",type(json_response))
    json_string = json.dumps(json_response, indent=4)
    print("JSON string: ", json_string)


def check_deleted_user(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("Check deleted user: ", user_id)
    response = requests.get(url, headers=headers)
    json_response = response.json()

    # Assert
    assert response.status_code == 404
    assert json_response["message"] == "Resource not found"


# Post Request
def post_request():
    # Setup
    url = base_url + "/public/v2/users/"
    print("Sending POST request to url: ", url)
    name = generate_random_name()
    email = generate_random_email()
    json_data = {
        "name": name,
        "email": email,
        "gender": "male",
        "status": "active"
    }

    # Act
    response = requests.post(url, data=json_data, headers=headers,)

    # Assert
    assert response.status_code == 201
    json_response = response.json()
    user_id = json_response["id"]
    assert json_response["name"] == name
    assert json_response["email"] == email
    json_string = json.dumps(json_response, indent=4)
    print("JSON string: ", json_string)

    return user_id


# PUT request
def put_request(user_id_to_update):
    url = base_url + f"/public/v2/users/{user_id_to_update}"
    print("Sending PUT request to url: ", url)
    new_name = generate_random_name()
    new_email = generate_random_email()
    json_data = {
        "name": new_name,
        "email": new_email
    }
    response = requests.put(url, data=json_data, headers=headers)

    # Assert
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["name"] == new_name
    assert json_response["email"] == new_email
    json_string = json.dumps(json_response, indent=4)
    print("After modifying data: " + json_string)


# DELETE request
def delete_request(user_id_to_delete):
    url = base_url + f"/public/v2/users/{user_id_to_delete}"
    print("Sending DELETE request to url: ", url)
    response = requests.delete(url, headers=headers)

    # Assert
    assert response.status_code == 204


# Call methods

get_request()
user_id = post_request()
put_request(user_id)
delete_request(user_id)
check_deleted_user(user_id)
