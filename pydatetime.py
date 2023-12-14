from datetime import date
import calendar

ca = calendar
ca.day_name
print(ca.day_name)


today = date.today()
print(today.day)
print(today.month)
print(today.year)
print(today.weekday())

date_format = today.strftime("%A %dth of %B %Y")
next_year = today.replace(year=today.year + 1)
difference = abs(next_year - today)
print(date_format)
print(next_year)
print(difference)

