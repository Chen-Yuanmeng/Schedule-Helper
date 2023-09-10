from csv_parser import *


class Course:
    """
    课程类
    负责管理csv输入的信息, 生成对应的日历文本
    """

    pattern = """BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VTIMEZONE
TZID:UTC
BEGIN:STANDARD
DTSTART:16010101T000000
TZOFFSETFROM:+0000
TZOFFSETTO:+0000
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:16010101T000000
TZOFFSETFROM:+0000
TZOFFSETTO:+0000
END:DAYLIGHT
END:VTIMEZONE
BEGIN:VEVENT
SUMMARY;CHARSET=UTF-8:{name}
DTSTAMP:19700101T000000Z
STATUS:TENTATIVE
LOCATION;CHARSET=UTF-8:{location}
DESCRIPTION;CHARSET=UTF-8:{lecturer}
X-ALLDAY:0
X-TIMEZONE:Asia/Shanghai
DTSTART:{start}Z
DTEND:{end}Z{alarm}
END:VEVENT
END:VCALENDAR"""

    alarm = """
BEGIN:VALARM
ACTION:AUDIO
TRIGGER:-PT{trigger}M
DESCRIPTION:Reminder
END:VALARM"""

    class_table = None

    @classmethod
    def read_course_table(cls) -> None:
        cls.class_table = parse_arrangement()

    def __init__(self) -> None:
        self.name, self.lecturer, self.location, self.weeks, self.days, self.indexes = parse_courses()
        self.name: str
        self.lecturer: str
        self.location: str
        self.weeks: tuple[int]
        self.days: tuple[int]
        self.indexes: tuple[int]

        if not self.class_table:
            raise LookupError('class table not found')

    def __str__(self) -> str:
        pass
