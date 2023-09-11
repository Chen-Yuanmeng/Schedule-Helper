import csv


_arrangement_start: int = 12


def parse_arrangement(path: str = '设置课节.csv') -> dict[int, tuple[str]]:
    try:
        with open(path, encoding='UTF-8') as fp:
            return {int(itm[0]): tuple(itm[1:3]) for idx, itm in enumerate(csv.reader(fp)) if idx > _arrangement_start and itm[0]}
    except UnicodeDecodeError:
        with open(path, encoding='GBK') as fp:
            return {int(itm[0]): tuple(itm[1:3]) for idx, itm in enumerate(csv.reader(fp)) if idx > _arrangement_start and itm[0]}

