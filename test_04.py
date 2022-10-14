from typing import Dict
from enum import Enum, unique
import calendar
import itertools


@unique
class Week(Enum):
    MONDAY=calendar.MONDAY
    TUESDAY = calendar.TUESDAY
    WEDNESDAY = calendar.WEDNESDAY
    THURSDAY = calendar.THURSDAY
    FRIDAY = calendar.FRIDAY
    SATURDAY = calendar.SATURDAY
    SUNDAY = calendar.SUNDAY

    _labels: Dict['Week', str]

    def to_label(self) -> str:
        return self._labels[self]


Week._labels = {
    Week.MONDAY: "月",
    Week.TUESDAY: "火",
    Week.WEDNESDAY: "水",
    Week.THURSDAY: "木",
    Week.FRIDAY: "金",
    Week.SATURDAY: "土",
    Week.SUNDAY: "日"
}


class CalenderService:

    def __init__(self, year, month):
        self.year = year
        self.month = month

    def get_calendar(self) -> str:
        return calendar.month(self.year, self.month)

    def get_calendar_month_list(self) -> list:
        c = calendar.Calendar(firstweekday=6)  # 日曜始まりのカレンダークラス
        return c.monthdays2calendar(self.year, self.month)

    def get_month_length(self) -> int:
        c = calendar.Calendar(firstweekday=6)  # 日曜始まりのカレンダークラス
        cal = c.monthdays2calendar(self.year, self.month)
        day_week_list = list(itertools.chain.from_iterable(cal))
        without_zero_paddings = [d for d in day_week_list if d[0] != 0]
        return len(without_zero_paddings)

    def get_week(self, day: int) -> Week:
        c = calendar.Calendar(firstweekday=6)  # 日曜始まりのカレンダークラス
        cal = c.monthdays2calendar(self.year, self.month)
        day_week_list = list(itertools.chain.from_iterable(cal))
        without_zero_paddings = [d for d in day_week_list if d[0] != 0]
        week_code = None
        for d in without_zero_paddings:
            if d[0] == day:
                week_code = d[1]
        return Week(week_code)


cal = CalenderService(year=2012, month=1)
print(cal.get_calendar())
print(cal.get_calendar_month_list())
print(cal.get_month_length())
print(cal.get_week(day=1))
print(cal.get_week(day=1).to_label())
