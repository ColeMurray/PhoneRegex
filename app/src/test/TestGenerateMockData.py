'''

Test cases for Generating Mock Data
'''
import unittest

from PhoneRegex.app.src.generateMockData import get_file, get_random_phone_number, get_random_name_from_file, \
    LOC_OF_FIRST_NAME_FILE, LOC_OF_LAST_NAME_FILE, get_list_of_mock_customer_info


class TestGenerateMockData(unittest.TestCase):
    def test_file_open_properly_should_be_not_none(self):
        first_name_file = get_file(LOC_OF_FIRST_NAME_FILE)
        assert first_name_file is not None

        last_name_file = get_file(LOC_OF_LAST_NAME_FILE)
        assert last_name_file is not None

    def test_get_random_name_should_return_not_null(self):
        first_name = get_random_name_from_file(LOC_OF_LAST_NAME_FILE).title()
        last_name = get_random_name_from_file(LOC_OF_FIRST_NAME_FILE).title()
        print 'Full name is %s %s' % (first_name, last_name)
        assert isinstance(last_name, str)
        assert isinstance(first_name, str)
        assert last_name is not None
        assert first_name is not None

    def test_get_random_number_should_be_length_7_or_8(self):
        phone_num = get_random_phone_number()
        assert (len(phone_num) == 7 or (len(phone_num) == 8 and phone_num.__contains__('-')))

    def test_get_mock_data_of_size_n_should_return_list_of_size_n(self):
        n = 10
        customer_info = get_list_of_mock_customer_info(n)
        assert (len(customer_info) == n)





