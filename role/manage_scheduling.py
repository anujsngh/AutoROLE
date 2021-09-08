from role import schedule, logging, start_time, end_time, dt
from role.manage_time import is_right_time, is_frequent_time, is_break_time
from role.manage_session import session_manager
from role.utils import get_scrap_interval


def session_schedule_manager():
    logging.info("session_schedule_manager had started for today")

    while True:
        if is_right_time():
            scrap_interval = get_scrap_interval()
            schedule.every(scrap_interval).seconds.do(session_manager)
            if is_frequent_time():
                while True:
                    if is_break_time():
                        break
                    schedule.run_pending()

            elif is_break_time():
                while True:
                    if is_frequent_time():
                        break
                    schedule.run_pending()

            elif not (is_break_time() and is_frequent_time()):
                while True:
                    if is_break_time() and is_frequent_time():
                        break
                    schedule.run_pending()
        else:
            break

    logging.info("session_schedule_manager had stopped for today")


def schedule_manager():
    logging.info("schedule_manager had started")

    schedule.every().day.at(start_time[:-4]).do(session_schedule_manager)
    while True:
        schedule.run_pending()

    logging.info("schedule_manager had stopped")

