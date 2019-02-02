import os
import sys
import datetime
import copy
from utils import print_schedule
from templates import templates

def select_template(template_list):
    print(f'\nThese are templates you can use: {template_list}\n')
    
    text = input('Type a template you want to use: ')

    if text not in template_list:
        print(f'\nThere is not `{text}` templae\n\nPlease run again!\n')
        sys.exit()
    
    check = input(f'\nDo you want to use `{text}`? y/n : ')
    
    if check == 'y' :
        print(f'\nUsing `{text}` template...\n')
        template = templates.templates[text]
        return template
    else :
        return select_template(template_list)

def submit_schedule(template):
    schedule = copy.deepcopy(template)
    year = int(input('Put the year: '))
    month = int(input('Put the month: '))
    temp_day = 0

    for week, days in schedule.items():
        print(f'\nIn, {week}\n')
        for i in range(len(days)):
            day = int(input(f'Put the date for {days[i]}: '))
            
            if day < temp_day :
                month += 1
                if month > 12 :
                    year += 1
                    month = 1
            
            date = datetime.datetime(year, month, day).strftime('%Y%m%d')
            schedule[week][i] = date
            temp_day = day
    
    print('\nYour schedule is:\n')
    print_schedule(schedule)

    check = input(f'\nDo you want to use this schedule? y/n : ')
    
    if check == 'y' :
        print('Using the schedule')
        return schedule
    else :
        return submit_schedule(template)

template_list = [key for key in templates.templates]
template = select_template(template_list)
schedule = submit_schedule(template)