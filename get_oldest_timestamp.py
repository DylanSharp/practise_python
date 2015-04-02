import datetime

def timestamp_oldest(*kwargs):
    times = []
    for item in kwargs:
        times.append(item)
    times.sort()
    out = datetime.datetime.fromtimestamp(times[0])

    return out

print(timestamp_oldest(4,45,648,486,6,6,65,1, 8,48,2,2,4,6,8,4))



starter = datetime.datetime(2015, 10, 21, 16, 29)

def time_machine(int, type_string):
    td = datetime.timedelta()

    if type_string == "minutes":
        td = datetime.timedelta(minutes=int)
    elif type_string == "hours":
        td = datetime.timedelta(hours=int)
    elif type_string == "days":
        td = datetime.timedelta(days=int)
    elif type_string == "years":
        td = datetime.timedelta(days=(int*365))

    return starter + td

print(time_machine(5, "years"))

