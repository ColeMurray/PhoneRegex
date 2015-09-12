# GenerateMockData.py
# Creates a .csv file
# consisting of person, (optional)
# city, and phone number tuples
# ie. John Doe, 555-5555
# ie. John Doe, 555-5555
#
# Numbers can also be improperly
# formatted
# ie. John Doe, 55555555
#
from os import path
import random

LOC_OF_FIRST_NAME_FILE = path.abspath(__file__ + '/../../../data/names.txt')
LOC_OF_LAST_NAME_FILE = path.abspath(__file__ + '/../../../data/last_names.txt')


class CustomerInfo(object):
    def __init__(self, full_name, phone_num):
        self.full_name = full_name
        self.phone_num = phone_num

    def __repr__(self):
        return 'Customer: ' + str(self.full_name) + ' ' + str(self.phone_num)


'''
Creates a file with the provided name. The file
will contain @param row_count customer entries

ie. John Doe 555-5555

'''


def create_file_of_mock_data(file_name, row_count):
    customer_list = get_list_of_mock_customer_info(row_count);
    my_file = open(file_name, "w+")
    for customer in customer_list:
        my_file.write("%s\n" % customer)
    my_file.close()
    return my_file


def get_list_of_mock_customer_info(customer_amount):
    customer_info_list = []
    for i in range(0, customer_amount):
        customer = CustomerInfo(get_random_full_name(), get_random_phone_number())
        customer_info_list.append(customer)

    return customer_info_list


def get_file(file_loc):
    my_file = open(file_loc, 'r')
    return my_file


def get_random_full_name():
    full_name = get_random_name_from_file(LOC_OF_FIRST_NAME_FILE).title() + ' ' + get_random_name_from_file(
        LOC_OF_LAST_NAME_FILE).title()
    return full_name


def get_random_name_from_file(file_loc):
    my_file = get_file(file_loc)
    content = []
    if my_file is not None:
        for line in my_file:
            content.append(line.rstrip())

    random_index = random.randint(0, len(content))

    return content[random_index].title()


def get_random_phone_number():
    dash = '-' if random.randint(0, 1) == 1 else ''
    rand_num = str(random.randint(10 ** 6, 10 ** 7 - 1))
    rand_num = rand_num[:3] + dash + rand_num[3:]
    return rand_num
