import unittest
import os
from unittest.mock import patch

from calendar import select_template, submit_schedule, write_new_calendar

class CalendarTestCase(unittest.TestCase):

    def setUp(self):
        self.templates = [
            {
                "name": "template1",
                "schedule" : {
                    "week1": ['day1', 'day2', 'day3']
                }
            },
            {
                "name": "template2",
                "schedule" : {
                    "week1": ['day1', 'day2', 'day3']
                }
            }
        ]

        self.template = {
            "name": "test",
            "schedule" : {
                "week1": ['day1', 'day2', 'day3']
            }
        }
    
    def test_user_selecte_template_on_a_template_list(self):
        
        user_input = [
            '1',
            'y'
        ]

        expected_output = {
            "name": "template1",
            "schedule" : {
                "week1": ['day1', 'day2', 'day3']
            }
        }

        with patch('builtins.input', side_effect=user_input):
            template = select_template(self.templates)
        self.assertEqual(template, expected_output)

    def test_user_selecte_template_does_not_exist_on_the_list(self):
        
        user_input = [
            '0',
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
            "name": "test",
            "schedule": {
                "week1": ['20190201', '20190202', '20190203']
            }
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
            "name": "test",
            "schedule": {
                "week1": ['20190228', '20190301', '20190302']
            }
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
            "name": "test",
            "schedule": {
                "week1": ['20191231', '20200101', '20200102']
            }
        }

        with patch('builtins.input', side_effect=user_input):
            schedule = submit_schedule(self.template)
        self.assertEqual(schedule, expected_output)

    def test_create_correct_new_calendar_in_output_folder(self):
        schedule = {
            "name": "test",
            "schedule": {
                "week1": ['20190201', '20190202', '20190203']
            }
        }
        
        write_new_calendar(schedule)
        
        self.assertTrue(os.path.exists(f'./output/{schedule["name"]}'))

if __name__ == '__main__':
    unittest.main()