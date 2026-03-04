from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import core.parse_date
from icalendar import Alarm, Event as ICalEvent


class Event:
    def __init__(self, course, week: int, day: int):
        self.name, self.lecturer, self.location = course.info()
        self.week = week
        self.day = day
        self.sect = course.sect
        self.alarm = course.alarm
        ...

    def generate_event(self, origin, sect_time, timezone: str):
        date = core.parse_date.parse_date(origin, self.week, self.day)
        tz = ZoneInfo(timezone)
        start = datetime.strptime(date + sect_time[min(self.sect)][0], '%Y%m%d%H%M%S').replace(tzinfo=tz)
        end = datetime.strptime(date + sect_time[max(self.sect)][1], '%Y%m%d%H%M%S').replace(tzinfo=tz)

        event = ICalEvent()
        event.add('summary', self.name)
        event.add('status', 'TENTATIVE')
        event.add('location', self.location)
        event.add('description', self.lecturer)
        event.add('dtstart', start)
        event.add('dtend', end)

        if self.alarm is not None:
            alarm = Alarm()
            alarm.add('action', 'AUDIO')
            alarm.add('trigger', timedelta(minutes=-self.alarm))
            alarm.add('description', 'Reminder')
            event.add_component(alarm)

        return event
