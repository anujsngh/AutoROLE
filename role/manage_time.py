from role import pd, dt


def convert_12_to_24_time(time_in_12=None, in_str=False):
    if time_in_12:
        time_in_24 = dt.datetime.strptime(str(time_in_12), "%I:%M%p").time()
        if in_str:
            return str(time_in_24)
        return time_in_24


def is_frequent_time():
    pass


def is_college_day(date):
    # checks if today is in monday - friday range (is a business day)
    return bool(len(pd.bdate_range(date, date)))


def time_in_range(current=None, start=None, end=None):
    if current and start and end:
        return start <= current <= end


def is_right_time():
    current_datetime = dt.datetime.now()
    current_date = current_datetime.strftime("%Y-%m-%d")
    start_datetime = pd.to_datetime(str(current_datetime.date()) + " 10:30")
    end_datetime = pd.to_datetime(str(current_datetime.date()) + " 16:30")

    return time_in_range(current=current_datetime, start=start_datetime, end=end_datetime) and is_college_day(current_date)

