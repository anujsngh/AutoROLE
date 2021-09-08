from role import logging
from role.manage_notification import show_notification
from role.manage_time import is_right_time, is_ahead_right_time, is_behind_right_time
from role.manage_session import session_manager
from role.manage_scheduling import schedule_manager, session_schedule_manager


def scrap_manager():
    logging.info("scrap_manager had Started")

    while True:
        try:
            if is_behind_right_time():
                schedule_manager()
                break

            elif is_ahead_right_time():
                session_manager()
                session_schedule_manager()
                break

            elif is_right_time():
                session_manager()
                schedule_manager()
                break

            logging.info("scrap_manager had Stopped")

        except Exception as err:
            logging.error(f"Error at Scrap Manager : {err}", stack_info=True)
            show_notification(title="Error Occurred at Scrap Manager !!!", message_text=err)
            continue


