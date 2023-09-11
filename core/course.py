import core.event


class Course:
    """
    课程类

    负责管理csv输入的信息, 生成对应的日历文本
    """

    def __init__(self, item: tuple[str, str, str, tuple[int], tuple[int], tuple[int]], alarm: int | None, origin):
        self.name, self.lecturer, self.location, self.weeks, self.days, self.sect = item
        self.alarm = alarm
        self.origin = origin

    def info(self):
        return self.name, self.lecturer, self.location

    def iterate(self, origin, sect_time, output):
        for w in self.weeks:
            for d in self.days:
                print(core.event.Event(self, w, d).generate_event_text(origin, sect_time), file=output, end='')
