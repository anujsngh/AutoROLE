from role import pd, dt, cwdir_name, start_time, end_time


current_datetime = dt.datetime.now()
start_datetime = pd.to_datetime(str(current_datetime.date()) + " " + str(start_time))
end_datetime = pd.to_datetime(str(current_datetime.date()) + " " + str(end_time))
current_date = current_datetime.strftime("%Y-%m-%d")
weekday_list = ["monday", "tuesday", "wednesday", "thursday", "friday"]


def convert_12_to_24_time(time_in_12=None, in_str=False):
    if time_in_12:
        time_in_24 = dt.datetime.strptime(str(time_in_12), "%I:%M%p").time()
        if in_str:
            return str(time_in_24)
        return time_in_24


def is_frequent_time():
    frequent_time_df = pd.read_csv("/".join([cwdir_name, "/resources/frequent_times.csv"]))
    for _, data in frequent_time_df.iterrows():
        startdatetime = pd.to_datetime(current_date + " " + data["starttime"])
        enddatetime = pd.to_datetime(current_date + " " + data["endtime"])
        if (startdatetime <= current_datetime <= enddatetime) and (dt.date.today().weekday() <= len(weekday_list)):
            if weekday_list[dt.date.today().weekday()] == data["weekday"]:
                return True
    return False


def is_break_time():
    break_time_df = pd.read_csv("/".join([cwdir_name, "/resources/time_table.csv"]))
    for _, data in break_time_df.iterrows():
        startdatetime = pd.to_datetime(current_date + " " + data["starttime"])
        enddatetime = pd.to_datetime(current_date + " " + data["endtime"])
        if not (startdatetime <= current_datetime <= enddatetime):
            return True
    return False


def is_college_day(date):
    # checks if today is in monday - friday range (is a business day)
    return bool(len(pd.bdate_range(date, date)))


def is_right_time():
    return (start_datetime <= current_datetime <= end_datetime) and is_college_day(current_date)


def is_ahead_right_time():
    return current_datetime > start_datetime


def is_behind_right_time():
    return current_datetime < start_datetime


def is_not_right_time():
    return current_datetime > end_datetime


if __name__ == '__main__':
    print(is_frequent_time())

