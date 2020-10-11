# Counting Sundays
# Project Euler - Problem 19
# Sean Malloy
from datetime import date

begin_year = 1901
end_year = 2000
begin_month = 1
end_month = 12

sun_count = 0
for year in range(begin_year, end_year + 1):
	for month in range(begin_month, end_month + 1):
		if date(year, month, 1).ctime().split()[0] == 'Sun':
			sun_count += 1

print(sun_count)
