import csv
import re
from typing import Iterable

_argm_start: int = 12
_crs_start: int
_transtable = str.maketrans({'，': ' ', '、': ' ', '~': '-', ',': ' '})

_prepr_regex = re.compile(r'\s+')
_sep_regex = re.compile(r'(\d+)\s+')
_range_regex = re.compile(r'(\d+)-(\d+)')


def parse_arrangement(path: str = '设置课节.csv', encoding: str = "UTF-8") -> dict[int, tuple[str]]:
    with open(path, encoding=encoding) as fp:
        return {int(itm[0]): tuple(itm[1:3]) for idx, itm in enumerate(csv.reader(fp)) if idx > _argm_start and itm[0]}


def parse_courses(path: str = '设置课程.csv', encoding: str = "UTF-8") -> list[tuple[str | tuple[int]]]:
    with open(path, encoding=encoding) as fp:
        return [(n, lcr, pos, *_range_handler(rst)) for idx, (n, lcr, pos, *rst) in enumerate(csv.reader(fp)) if idx > _crs_start and n]


def _range_handler(args: Iterable[str]) -> Iterable[Iterable[int]]:
    lst = []
    for i in args:
        i = _prepr_regex.sub(' ', i).translate(_transtable)
        lst.extend((int(j.group(1)) for j in _sep_regex.finditer(i)),)
        for k in _range_regex.finditer(i):
            lst.extend(range(int(k.group(1)), int(k.group(2))+1))
    yield lst


__all__ = [parse_arrangement, parse_courses]

if __name__ == '__main__':
    # test
    s = '1、3、5-7，10,11  12~20'
    for i in _range_handler((s,)):
        print(i)