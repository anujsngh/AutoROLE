from manage_time import is_right_time, is_frequent_time


def get_scrap_interval():
    if is_right_time():
        scrap_speed = 5
        if is_frequent_time():
            scrap_speed = 3
    else:
        scrap_speed = 7.5

    return scrap_speed * 60


if __name__ == '__main__':
    print(is_right_time())
