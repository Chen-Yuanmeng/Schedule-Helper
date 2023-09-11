import re
import csv
from typing import Iterable


_course_start: int = 13
_transtable = str.maketrans({'，': ' ', '、': ' ', '~': '-', ',': ' ', '\\': ' ', '/': ' '})

_prepr_regex = re.compile(r'\s+')
_sep_regex = re.compile(r'(\d+)\s*')
_range_regex = re.compile(r'(\d+)-(\d+)')


def parse_courses(path: str = '设置课程.csv') -> list[tuple[str | tuple[int]]]:
    try:
        with open(path, encoding='UTF-8') as fp:
            return [(n, lcr, pos, *_range_handler(rst)) for idx, (n, lcr, pos, *rst, _) in enumerate(csv.reader(fp)) if idx > _course_start and n]
    except UnicodeDecodeError:
        with open(path, encoding='GBK') as fp:
            return [(n, lcr, pos, *_range_handler(rst)) for idx, (n, lcr, pos, *rst, _) in enumerate(csv.reader(fp)) if idx > _course_start and n]


def _range_handler(args: Iterable[str]) -> Iterable[tuple[int]]:
    for i in args:
        s = set()
        i = _prepr_regex.sub(' ', i).translate(_transtable)
        s.update((int(j.group(1))) for j in _sep_regex.finditer(i))
        for k in _range_regex.finditer(i):
            s.update(range(int(k.group(1)), int(k.group(2))+1))
        yield tuple(s)


__all__ = [parse_courses]
