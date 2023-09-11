#find what the day is on the date given
import calendar
month,day,year = map(int,input().split("/"))
dayId = calendar.weekday(year,month,day)
print(calendar.day_name[dayId].upper())

'''
output:
2/19/1996
MONDAY
'''