from PhoneRegex.app.src.PhoneRegex import parse_phone_number, format_phone_number

__author__ = 'User'

import unittest


class TestPhoneRegex(unittest.TestCase):
    def test_phone_parse_should_return_generic_fake_number(self):
        fake_string = 'John Doe 555-5555'
        expected = '555-5555'
        result = parse_phone_number(fake_string)
        print result
        assert result == expected

    def test_phone_with_area_code_should_assert_true(self):
        fake_string = 'John Doe (555)555-5555'
        expected = '(555)555-5555'
        result = parse_phone_number(fake_string)
        print result
        assert result == expected


    def test_format_phone_should_return_generic_fake_number(self):
        fake_number = '(555)-555-5555'
        expected = '5555555555'
        result = format_phone_number(fake_number)
        assert result == expected

