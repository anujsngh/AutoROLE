from role.manage_time import is_right_time, is_frequent_time
from role import ConfigParser, config_dict


def get_scrap_interval():
    if is_right_time():
        scrap_speed = float(config_dict["scrap_settings"]["normal_scrap_speed"])
        if is_frequent_time():
            scrap_speed = float(config_dict["scrap_settings"]["fast_scrap_speed"])
    else:
        scrap_speed = float(config_dict["scrap_settings"]["slow_scrap_speed"])
    scrap_interval = int(scrap_speed * 60)
    return scrap_interval


if __name__ == '__main__':
    print(get_scrap_interval())
