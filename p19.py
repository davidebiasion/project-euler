def days_of_month_year(month, year):
	# leap years
	if month==1:
		if year%4==0:
			if year%100==0:
				if year%400==0:
					#print("leap:", year)
					return 29
			else:
				#print("leap:", year)
				return 29

	days = {
		0: 31,
		1: 28,
		2: 31,
		3: 30,
		4: 31,
		5: 30,
		6: 31,
		7: 31,
		8: 30,
		9: 31,
		10: 30,
		11: 31	
	}

	return days[month]


# 1 jan 1900, monday
curr_month = 0
curr_year = 1900
day_of_the_week = 0
sundays_on_first_of_the_month = 0


while True:
	# first day of the month
	day_of_the_week = (day_of_the_week+days_of_month_year(curr_month, curr_year))%7
	curr_month = (curr_month+1)%12
	if curr_month==0:
		curr_year+=1

	# stop on 1 jan 2001
	if curr_year==2001:
		break

	#print("month:", curr_month, "year:", curr_year, "day:", day_of_the_week)

	# first day on the month is sunday
	if day_of_the_week==6 and curr_year>=1901:
		sundays_on_first_of_the_month+=1


print(sundays_on_first_of_the_month)

