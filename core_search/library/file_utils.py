import json


def read(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    return data



