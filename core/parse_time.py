def parse_time(time: str) -> str:
    """
    把输入的时间（东八区）h或hh或h:mm或hh:mm或h:mm:ss或hh:mm:ss
    转化为格林尼治时间hhmmss格式
    """
    time_lst = time.replace('：', ':').split(':')
    if len(time_lst) == 1:
        hour, = time_lst
        minute = second = '0'
    elif len(time_lst) == 2:
        hour, minute = time_lst
        second = '0'
    elif len(time_lst) == 3:
        hour, minute, second = time_lst
    else:
        raise ValueError(f'无法解析时间{time}: 输入错误')
    hour, minute, second = int(hour), int(minute), int(second)
    if hour < 8:
        hour += 16
    else:
        hour -= 8
    return f'{hour:02}{minute:02}{second:02}'

