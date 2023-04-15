import requests
from dotenv import load_dotenv
import os


def lst_to_dict(some_list):
    dct = {}
    temporary_dct = {}
    count = len(some_list) - 1
    for i in some_list[:-1]:
        if i == some_list[0]:
            dct[some_list[count - 1]] = some_list[count]
        else:
            dct[some_list[count - 1]] = temporary_dct
        temporary_dct = dct.copy()
        dct.clear()
        count -= 1
    return temporary_dct


def filter_(geo_logs):
    res_dict = []
    for diction in geo_logs:
        items = diction.items()
        for item in items:
            country = item[1][1]
            if country == "Россия":
                res_dict.append(diction)
    return res_dict


def find_unique(ids):
    new = []
    for key, value in ids.items():
        for item in value:
            if item not in new:
                new.append(item)
    return new


def find_max(stats):
    company = ""
    max_ = 0
    for name, number in stats.items():
        if number > max_:
            max_ = number
            company = name
    return company


load_dotenv()
ya_token = os.getenv('ya_token')
ya_password = os.getenv('ya_password')
email = os.getenv('email')
link_create_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
link_list_of_files = 'https://cloud-api.yandex.net/v1/disk/resources/public'
wrong_link = 'https://cloud-api.yandex.net/v1/disk/resources/public6'
params = {'path': 'test'}
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'OAuth {}'.format(ya_token)
}


def create_folder():
    response = requests.put(link_create_folder, headers=headers, params=params)
    return response.status_code


def check_folder():
    response = requests.get(link_list_of_files, headers=headers, params=params)
    return response.status_code


def failure_function():
    response = requests.get(wrong_link, headers=headers, params=params)
    return response.status_code