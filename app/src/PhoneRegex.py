import re

__author__ = 'User'

'''
Parse a phone number from a given line
'''


def parse_phone_number(string_to_parse):
    phone_regex_pattern = r'([\(]?[0-9]{3,3}[\)]?)?[-]?[0-9]{3,3}[-]?[0-9]{4,4}'
    match = re.search(phone_regex_pattern, string_to_parse)
    if match is None:
        return ''
    return str(match.group())


'''
Returns a phone number formatted
with only numbers
'''


def format_phone_number(phone_number):
    phone_regex_pattern = r'[0-9]+'
    match = re.findall(phone_regex_pattern, phone_number)
    formatted = ''
    for c in match:
        formatted += str(c)

    return formatted
