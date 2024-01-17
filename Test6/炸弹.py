import datetime
date_str = input()
days = int(input())

year, month, day = map(int,date_str.split(","))
date = datetime.date(year, month, day)
delta = datetime.timedelta(days=days)

explosion_date = date + delta
explosion_date_str = explosion_date.strftime("%Y-%m-%d")
print(explosion_date_str)