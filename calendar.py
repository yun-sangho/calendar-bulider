import os
import sys
import datetime
import copy
import re
from utils import get_names_from_templates, print_schedule
from templates import templates


def select_template(templates):

    names = get_names_from_templates(templates)

    num = int(
        input("Type a number of template that you want to use: ")
    )

    if num - 1 not in range(len(names)):
        print(
            f"\nThere is not `{num}: {names[num - 1]}` templae\n\nPlease run again!\n"
        )
        sys.exit(1)

    check = input(
        f"\nDo you want to use `{num}: {names[num - 1]}`? y/n : "
    )

    if check == "y":
        print(f"\nUsing `{num}` template...\n")
        template = templates[num - 1]
        return template
    else:
        return select_template(templates)


def submit_schedule(template):
    temp = copy.deepcopy(template)
    schedule = temp["schedule"]
    year = int(input("Type year: "))
    month = int(input("Type month: "))
    temp_day = 0

    for week, days in schedule.items():
        print(f"\nIn, {week}\n")
        for i in range(len(days)):
            day = int(input(f"Type date for {days[i]}: "))

            if day < temp_day:
                month += 1
                if month > 12:
                    year += 1
                    month = 1

            date = datetime.datetime(year, month, day).strftime(
                "%Y%m%d"
            )
            schedule[week][i] = date
            temp_day = day

    print("\nYour schedule is:\n")
    print_schedule(temp)

    check = input(f"\nDo you want to use this schedule? y/n : ")

    if check == "y":
        print("Using the schedule...\n")
        return temp
    else:
        return submit_schedule(template)


def write_new_calendar(schedule):
    date = datetime.datetime.now().strftime("%Y%m%d")

    PATH_TO_TEMPALTE = f'{os.getcwd()}/templates/{schedule["name"]}'
    PATH_TO_OUTPUT = f'{os.getcwd()}/output/{schedule["name"]}-{date}'

    if not os.path.exists(PATH_TO_OUTPUT):
        os.mkdir(PATH_TO_OUTPUT)

    for week, days in schedule["schedule"].items():
        print(f"\nStart writing, {week}...\n")

        with open(f"{PATH_TO_TEMPALTE}/{week}.ics", "r") as f:
            with open(f"{PATH_TO_OUTPUT}/{week}.ics", "w+") as o:
                for line in f:
                    if re.search(r"%DAY\d+%", line) is not None:
                        for i in range(len(days)):
                            text_to_search = f"%DAY{i + 1}%"
                            if text_to_search in line:
                                o.write(
                                    line.replace(
                                        text_to_search, days[i]
                                    )
                                )
                                break
                    elif "PRODID" in line:
                        temp_line = line.replace("\n", "")
                        o.write(f"{temp_line} {date}\n")
                    elif "*****" not in line:
                        o.write(line)
        o.close()
        f.close()
