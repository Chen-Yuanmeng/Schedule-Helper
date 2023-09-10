import icalendar
from datetime import datetime, timedelta


# # 以格林尼治时间存储
sect_time = {1: ('000000', '005000'), 2: ('005000', '014000'), 3: ('020000', '025000'), 4: ('025000', '034000'),
             5: ('053000', '062000'), 6: ('062000', '071000'), 7: ('072000', '081000'), 8: ('081000', '090000'),
             9: ('101000', '110000'), 10: ('110000', '115000'), 11: ('120000', '125000'), 12: ('125000', '134000')}


def generate_date(week: int, day: int) -> str:
    origin = datetime(2023, 8, 27)
    delta = timedelta(weeks=week, days=day)
    return icalendar.vDate(origin + delta).to_ical().decode()


def generate_start(week, day, sect):
    return generate_date(week, day) + 'T' + sect_time[min(sect)][0]


def generate_end(week, day, sect):
    return generate_date(week, day) + 'T' + sect_time[max(sect)][1]
