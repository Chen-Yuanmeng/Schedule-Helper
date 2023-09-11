from datetime import timedelta, datetime


def parse_date(origin: datetime, week: int, day: int) -> str:
    new = origin + timedelta(weeks=week - 1, days=day-1)
    return f'{new.year:04}{new.month:02}{new.day:02}'
