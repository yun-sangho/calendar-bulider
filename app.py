from calendar import (
    select_template,
    submit_schedule,
    write_new_calendar,
)
from templates import templates

template = select_template(templates)
schedule = submit_schedule(template)
write_new_calendar(schedule)
