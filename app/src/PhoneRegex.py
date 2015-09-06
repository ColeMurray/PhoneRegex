import re

__author__ = 'User'

'''
Parse a phone number from a given line
'''


def parse_phone_number(phone_num):
    phone_regex_pattern = r'([\(]?[0-9]{3,3}[\)]?)?[0-9]{3,3}[-]*[0-9]{4,4}'
    match = re.search(phone_regex_pattern, phone_num)
    if match is None:
        return ''
    return match.group()


