from datetime import datetime,time
def date_diff_in_seconds(dt2,dt1):
    timedelta = dt2 - dt1
    return timedelta.days * 24 * 3600 + timedelta.seconds
date1 = datetime.strptime('2005-04-21 20:20:00', '%Y-%m-%d %H:%M:%S')
date2 = datetime.now()
print(date_diff_in_seconds(date2,date1))
