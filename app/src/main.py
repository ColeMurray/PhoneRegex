from os import path
from os.path import dirname

import generateMockData
import PhoneRegex as phone_regex

__author__ = 'User'

DATA_PATH = path.abspath(dirname(dirname(dirname(__file__))) + '/data/')
print DATA_PATH

file_name = path.join(DATA_PATH, 'customer_doc.txt')
output_file_name = 'phone_numbers_only.txt'
row_count = 100
my_file = generateMockData.create_file_of_mock_data(file_name, row_count)
my_file = open(file_name, 'r')

out_file = open(path.join(DATA_PATH, output_file_name), 'w+')

for line in my_file:
    phone_number = phone_regex.parse_phone_number(line)
    phone_number = phone_regex.format_phone_number(phone_number)

    out_file.write('%s\n' % phone_number)

my_file.close()
out_file.close()
