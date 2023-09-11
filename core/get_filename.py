from datetime import datetime


def get_filename():
    return datetime.now().strftime("%Y%m%d_%H%M%S") + '.ics'
