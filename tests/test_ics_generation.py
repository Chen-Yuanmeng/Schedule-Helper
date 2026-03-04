import unittest
from datetime import datetime

from icalendar import Calendar

import core.course
import core.event
import core.parse_sect


class TestICSGeneration(unittest.TestCase):
    def test_event_contains_selected_timezone(self):
        item = ('高等数学', '张老师', 'A101', (1,), (1,), (1,))
        course = core.course.Course(item, None, datetime(2024, 9, 2))
        sect_time = core.parse_sect.parse_sect({1: ('8:00', '8:45')})

        event = core.event.Event(course, 1, 1).generate_event(datetime(2024, 9, 2), sect_time, 'Asia/Shanghai')
        ical_text = event.to_ical().decode('utf-8')

        self.assertIn('DTSTART;TZID=Asia/Shanghai:20240902T080000', ical_text)
        self.assertIn('DTEND;TZID=Asia/Shanghai:20240902T084500', ical_text)

    def test_calendar_can_be_parsed_in_non_default_timezone(self):
        item = ('Physics', 'Dr. Lee', 'Room 1', (1,), (1,), (1,))
        course = core.course.Course(item, 15, datetime(2024, 9, 2))
        sect_time = core.parse_sect.parse_sect({1: ('8:00', '8:45')})

        calendar = Calendar()
        calendar.add('prodid', '-//Schedule Helper//')
        calendar.add('version', '2.0')
        calendar.add_component(core.event.Event(course, 1, 1).generate_event(datetime(2024, 9, 2), sect_time, 'America/New_York'))

        parsed = Calendar.from_ical(calendar.to_ical())
        events = [component for component in parsed.walk() if component.name == 'VEVENT']

        self.assertEqual(len(events), 1)
        dtstart = events[0].decoded('dtstart')
        self.assertEqual(str(dtstart.tzinfo), 'America/New_York')


if __name__ == '__main__':
    unittest.main()
