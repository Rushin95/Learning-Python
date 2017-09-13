# Output the correct day in capital letters.
date = map(int, raw_input().split(' '))
import calendar
print calendar.day_name[calendar.weekday(date[2],date[0],date[1])].upper()

# Sample Input:
# 08 05 2015
