import calendar

m, d, y = map(int, input().split())
day_num = calendar.weekday(y, m, d)
day_name = calendar.day_name[day_num]
print(day_name.upper())