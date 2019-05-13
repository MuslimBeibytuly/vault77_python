import datetime
import pytz

# print(datetime.MINYEAR)
# print(datetime.MAXYEAR)

some_date = datetime.date(year=2019, month=5, day=13)

print(some_date.strftime('%d.%m.%Y'))

local_date_time = datetime.datetime(
    year=2019, month=5, day=13,
    hour=20, minute=6, second=0, 
    tzinfo=pytz.timezone('Asia/Almaty')
)