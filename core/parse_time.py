def parse_time(time: str) -> str:
    """
    把输入的时间 h或hh或h:mm或hh:mm或h:mm:ss或hh:mm:ss
    转化为本地时间 hhmmss 格式
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
    return f'{hour:02}{minute:02}{second:02}'
