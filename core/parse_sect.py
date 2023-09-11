import core.parse_time


def parse_sect(_d: dict):
    result = {}
    for i in _d.keys():
        result[i] = (core.parse_time.parse_time(_d[i][0]), core.parse_time.parse_time(_d[i][1]))
    return result
