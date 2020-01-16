# pylint: disable=invalid-name
"""
Count down to those special days in your life.
Week-end assumed as Sat-Sunday.
Feature list: None
"""
from datetime import datetime, timedelta

special_date = datetime(2020, 3, 2)
holiday_list = [
    datetime(2019, 11, 1),
    datetime(2019, 11, 2),
    datetime(2019, 11, 3),
    datetime(2019, 11, 4),
    datetime(2019, 11, 5),
    datetime(2019, 11, 6),
    datetime(2019, 11, 7),
    datetime(2019, 11, 8),
    datetime(2019, 11, 9),
    datetime(2019, 11, 10),
    datetime(2019, 11, 11),
    datetime(2019, 11, 12),
    datetime(2019, 11, 13),
    datetime(2019, 12, 21),
    datetime(2019, 12, 22),
    datetime(2019, 12, 23),
    datetime(2019, 12, 24),
    datetime(2019, 12, 25),
    datetime(2019, 12, 26),
    datetime(2019, 12, 27),
    datetime(2019, 12, 28),
    datetime(2019, 12, 29),
    datetime(2019, 12, 31),
    datetime(2020, 1, 1),
    datetime(2020, 1, 2),
    datetime(2020, 1, 3),
    datetime(2020, 1, 25),
    datetime(2020, 1, 26),
    datetime(2020, 1, 27),
    datetime(2020, 1, 28),
    datetime(2020, 2, 27),
    datetime(2020, 2, 28),
]
#
#
####### No more changes needed under here
#
#
workdays = 0
now = datetime(datetime.now().year, datetime.now().month, datetime.now().day)
day_tmp = now
holidays = 0
weekend = 0
while day_tmp < special_date:
    if day_tmp.weekday() in [5, 6]:
        weekend += 1
    elif day_tmp in holiday_list:
        holidays += 1
    else:
        workdays += 1
    day_tmp = day_tmp + timedelta(days=1)
total_days = (special_date - now).days
print("Days      to R        {} ".format(total_days))
print("Work Days to R        {:3d} ".format(workdays))
print("Weekend Days to R     {:3d} ".format(weekend))
print("Hol cnt               {:3d} ".format(holidays))
print(
    "Work/Leave balance {:5.2f}/{:5.2f}".format(
        100.0 * workdays / total_days, (100.0 * (weekend + holidays) / total_days)
    )
)
if (special_date - now).days == (workdays + weekend + holidays):
    print("Days compute correctly")
