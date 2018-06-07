import os
from datetime import datetime, timedelta

from chinese_calendar import is_holiday, is_workday


def get_next_workday(input_time):
    one_day = timedelta(days=1)
    input_time += one_day
    while is_holiday(input_time):
        input_time += one_day
    return input_time


if __name__ == '__main__':
    while True:
        if datetime.now().hour == 6 and datetime.now().minute == 0 and is_workday(datetime.now().date()):
            nextWorkDay = get_next_workday(datetime.now()).strftime('%Y-%m-%d')
            os.system("sudo rtcwake --mode mem --local --date '%s 08:20'" % nextWorkDay)
