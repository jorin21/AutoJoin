import datetime as dt

current_datetime = dt.datetime.now()
print(current_datetime)

string_date = current_datetime.strftime("%b %d, %I:%M:%S%p")
print(string_date)

if string_date == 'Apr 06, 12:09:00PM':
    print('yes!')
else:
    print('no')