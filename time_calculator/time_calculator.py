def add_time(start, duration, starting_day = False):

    am = True if (start.find("AM") != -1) else False
    hours = start.split(" ")[0]
    start_hours, start_minutes = hours.split(":")
    end_hours, end_minutes = duration.split(":")

    current_minutes, extra_hours = calculate_current_minutes(start_minutes, end_minutes, 0)

    current_hours, current_days, am = calculate_current_hours(start_hours, int(end_hours) + extra_hours, 0, am)

    if starting_day:
        current_day = calculate_current_day(starting_day, current_days)
        result = format_result(current_hours, current_minutes, am, current_days, current_day)
    else:
        result = format_result(current_hours, current_minutes, am, current_days)

    return result

def calculate_current_minutes(start, duration, hours): 
    current_minues = (int(start) + int(duration)) % 60

    hours = (int(start) + int(duration)) / 60

    return current_minues, int(hours)


def calculate_current_hours(start, duration, days, am):
    if int(start) + int(duration) < 12:
        if int(start) + int(duration) == 0:
            return 12, days, am
        else:
            return int(duration) + int(start), days, am

    if am:
        current_hours = int(start) + int(duration)

        if current_hours >= 12:
            current_hours = current_hours - 12
            am = False

        if current_hours >= 12:
            am = True
            days = days + 1
            duration = current_hours - 12
            return calculate_current_hours(0, duration, days, am)
        else:
            if current_hours == 0:
                current_hours = 12
            return current_hours, days, am
    else:
        current_hours = int(start) + int(duration)

        if current_hours > 12:
            am = True
            duration = current_hours - 12
            days = days + 1
            return calculate_current_hours(0, duration, days, am)
        else:
            return current_hours, days, am

def calculate_current_day(start_day, days):
    days_of_the_week = ["sunday","monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    current_day = start_day.lower()

    start_day_index = days_of_the_week.index(current_day)

    current_day = days_of_the_week[(days + start_day_index) % 7]


    return current_day

def format_result(current_hours, current_minutes, am, current_days, current_day = False):
    time = "AM" if am else "PM"
    current_minutes = '{:0>2}'.format(current_minutes)
    if current_day:
        current_day = current_day.capitalize()
        if current_days == 1:
            result = f"{current_hours}:{current_minutes} {time}, {current_day} (next day)"
        elif current_days > 1:
            result = f"{current_hours}:{current_minutes} {time}, {current_day} ({current_days} days later)"
        else:
            result = f"{current_hours}:{current_minutes} {time}, {current_day}"

    else:
        if current_days > 0:
            if current_days == 1:
                result = f"{current_hours}:{current_minutes} {time} (next day)"
            else:
                result = f"{current_hours}:{current_minutes} {time} ({current_days} days later)"
        else:
            result = f"{current_hours}:{current_minutes} {time}"

    return result
