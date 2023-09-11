import core.course
import core.parse_date


class Event:
    SEQ = """BEGIN:VEVENT
SUMMARY;CHARSET=UTF-8:{name}
DTSTAMP:19700101T000000Z
STATUS:TENTATIVE
LOCATION;CHARSET=UTF-8:{location}
DESCRIPTION;CHARSET=UTF-8:{lecturer}
X-ALLDAY:0
X-TIMEZONE:Asia/Shanghai
DTSTART:{start}
DTEND:{end}
{alarm}END:VEVENT
"""

    ALARM = """BEGIN:VALARM
ACTION:AUDIO
TRIGGER:-PT{trigger}M
DESCRIPTION:Reminder
END:VALARM
"""

    def __init__(self, course, week: int, day: int):
        self.name, self.lecturer, self.location = course.info()
        self.week = week
        self.day = day
        self.sect = course.sect
        self.alarm = course.alarm
        ...

    def generate_event_text(self, origin, sect_time):
        text = Event.SEQ
        text = text.replace('{name}', self.name)
        text = text.replace('{location}', self.location)
        text = text.replace('{lecturer}', self.lecturer)
        text = text.replace('{start}', core.parse_date.parse_date(origin, self.week, self.day) + 'T' + sect_time[min(self.sect)][0] + 'Z')
        text = text.replace('{end}', core.parse_date.parse_date(origin, self.week, self.day) + 'T' + sect_time[max(self.sect)][1] + 'Z')
        if self.alarm is None:
            text = text.replace('{alarm}', '')
        else:
            text = text.replace('{alarm}', Event.ALARM.replace('{trigger}', str(self.alarm)))
        return text
