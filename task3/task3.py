import json
import sys


def json_read(path):
    with open(path) as file:
        result = json.load(file)
    return result


def handle_value(obj):
    result = {}
    for elem in obj['values']:
        result[elem['id']] = elem['value']
    return result


def handle_dict(tests, values):
    if 'id' in tests.keys():
        key = tests['id']
        if key in values.keys():
            value = values[key]
            tests['value'] = value
    for key in tests.keys():
        if type(tests[key]) == list:
            handle_list(tests[key], values)


def handle_list(tests, values):
    for elem in tests:
        handle_dict(elem, values)


if __name__ == '__main__':
    tests = json_read(sys.argv[1])
    values = handle_value(json_read(sys.argv[2]))
    handle_dict(tests, values)
    with open("report.json", 'w') as outfile:
        json.dump(tests, outfile, indent=4)
