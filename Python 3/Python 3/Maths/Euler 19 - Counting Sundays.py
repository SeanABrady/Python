day = 1
counter = 0
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekdays =['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday']
months = ['January,' 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
          'November', 'December', 'January']

for year in range(1901,2001):
    month = 0
    if year % 4 == 0 and year % 100 != 0:
        monthDays[1] = 29
        if year % 400 == 0:
            monthDays[1] = 28
    else:
        monthDays[1] = 28

    for month in range(0,12):
        remainderDays = monthDays[month] % 7
        day += remainderDays
        if day > 6:
            day -= 7
        dayChecker = weekdays[day]
        if dayChecker == "Sunday":
            counter += 1
            if year == 2000 and month == 11:
                counter -= 1
        


    
    
    


