import requests
import json
from payLoad import *
import configparser
import os
from utilities.configurations import *
from utilities.resources import *

# -------------------------------------------------------------------------
# Setup
# print(current_directory)
config = get_config()  # method in file "configurations.py"

add_new_book_url = config["API"]["base_url"] + APIResources.add_book
get_book_url = config["API"]["base_url"] + APIResources.get_book_by_author

headers = {"Content-Type": "application/json"}


# -------------------------------------------------------------------------
# GET method
def send_get_request():
    response_get = requests.get(get_book_url, params={"AuthorName": "TMP"}, )
    assert response_get.status_code == 200
    print(response_get.json()[0]["book_name"])


# -------------------------------------------------------------------------
# POST method
def send_post_request():
    response_post = requests.post(add_new_book_url, json=addBookPayload("12342aa111a"), headers=headers)
    assert response_post.status_code == 200


# -------------------------------------------------------------------------
# Github API
# Get user info
def get_github_user():
    url = "https://api.github.com/user"
    github_response = requests.get(url, verify=False, auth=('phuocthanhpt', 'th@nhM@p0793*'))
    print(github_response)


# get_github_user()


def session_manager():
    ses = requests.session()
    ses.cookies.update({'visit-month': 'February'})
    # response = requests.get("https://httpbin.org/cookies", cookies={'visit-year': '2022'})
    response = ses.get("https://httpbin.org/cookies", cookies={'visit-year': '2022'})
    print(response.text)


session_manager()
