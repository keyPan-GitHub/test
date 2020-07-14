from datetime import datetime, timedelta


current_date = datetime.now()

print('Today is:'+ str(current_date))

today = datetime.now()

one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))


one_week = timedelta(weeks=1)
last_week = today - one_week
print('last_week was: ' + str(last_week))

