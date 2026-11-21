def time(minute):
    seconds = minute * 60
    hours = minute / 60
    return (seconds,hours)

print(time(30))
