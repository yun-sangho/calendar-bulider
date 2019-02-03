import unittest
from unittest.mock import patch

from calendar import select_template, submit_schedule

class CalendarTestCase(unittest.TestCase):

    def setUp(self):
        self.templates = {
            'template1' : {
                "week1": ['day1', 'day2', 'day3'],
            },
            'template2' : {
                "week1": ['day1', 'day2', 'day3', 'day4', 'day5']
            }
        }

        self.template = {
            "week1": ['day1', 'day2', 'day3']
        }
    
    def test_user_selecte_template_on_a_template_list(self):
        
        user_input = [
            'template1',
            'y'
        ]

        expected_output = {
            "week1": ['day1', 'day2', 'day3'],
        }

        with patch('builtins.input', side_effect=user_input):
            template = select_template(self.templates)
        self.assertEqual(template, expected_output)

    def test_user_selecte_template_does_not_exist_on_the_list(self):
        
        user_input = [
            'none',
        ]

        with patch('builtins.input', side_effect=user_input):
            with self.assertRaises(SystemExit) as cm:
                select_template(self.templates)
        
        self.assertEqual(cm.exception.code, 1)

    def test_submit_schedule_function_insert_date_into_template_correctly(self):

        user_input = [
            '2019',
            '2',
            '1',
            '2',
            '3',
            'y'
        ]

        expected_output = {
            "week1": ['20190201', '20190202', '20190203'],
        }

        with patch('builtins.input', side_effect=user_input):
            schedule = submit_schedule(self.template)
        self.assertEqual(schedule, expected_output)
    
    def test_submit_schedule_function_add_month_automaticaly(self):
        
        user_input = [
            '2019',
            '2',
            '28',
            '1',
            '2',
            'y'
        ]

        expected_output = {
            "week1": ['20190228', '20190301', '20190302'],
        }

        with patch('builtins.input', side_effect=user_input):
            schedule = submit_schedule(self.template)
        self.assertEqual(schedule, expected_output)

    def test_submit_schedule_function_add_year_automaticaly(self):
        
        user_input = [
            '2019',
            '12',
            '31',
            '1',
            '2',
            'y'
        ]

        expected_output = {
            "week1": ['20191231', '20200101', '20200102'],
        }

        with patch('builtins.input', side_effect=user_input):
            schedule = submit_schedule(self.template)
        self.assertEqual(schedule, expected_output)

if __name__ == '__main__':
    unittest.main()