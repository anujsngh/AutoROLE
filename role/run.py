from role import dt, logging, Service, webdriver, time, os, pd, schedule
from role.manage_notification import show_notification
from role.utils import get_scrap_speed
from role.manage_time import is_right_time
from role.manage_scrap import make_me_present, get_attendance_events, get_activity_links, get_sub_activity_list, do_login


def automate_attendance(cwdir_name=None, username=None, password=None):
    chromedriver_path = "/".join([cwdir_name, 'chromedriver'])
    c = 0
    while True:
        c += 1
        print(f'\nCurrent Time : {dt.datetime.strftime(dt.datetime.now(), "%Y-%m-%d %I:%M:%S%p")}\n')
        try:
            print("Starting Session ......\n")
            logging.info("Starting Session ......")
            service = Service(chromedriver_path)
            service.start()
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options = options.to_capabilities()
            driver = webdriver.Remote(service.service_url, options)

            do_login(driver=driver, username=username, password=password)

            attendance_card_list = get_attendance_events(driver=driver)

            attendance_link_list = get_activity_links(event_card_list=attendance_card_list)

            for attendance_link in attendance_link_list:
                driver.get(attendance_link)
                driver.implicitly_wait(10)
                status_link_list = get_sub_activity_list(driver=driver)
                make_me_present(driver=driver, status_link_list=status_link_list)

            driver.quit()
            print("\nEnding Session ......\n")
            logging.info("Ending Session ......")
            break
        except Exception as error:
            logging.error(f"Error : {error} at automate_attendance", stack_info=True)
            if c >= 5:
                break
            time.sleep(30)
            continue


def main():
    start_time = "10:15:00"
    end_time = "16:45:00"
    logging.info("Script started for today.")
    show_notification(title="Starting!!!", message_text="Script For Automating ROLE is Starting For Today......")
    while True:
        try:
            if is_right_time():
                cwd_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__))).replace('\\', '/')
                user_name = os.environ.get('ROLE_USERNAME')
                user_pass = os.environ.get('ROLE_PASSWORD')

                automate_attendance(cwdir_name=cwd_name, username=user_name, password=user_pass)
                schedule.every(5).minutes.do(automate_attendance, cwdir_name=cwd_name, username=user_name,
                                             password=user_pass)
                while True:
                    if is_right_time():
                        schedule.run_pending()
                    elif dt.datetime.now() > pd.to_datetime(str(dt.datetime.now().date()) + " " + start_time):
                        break
                    else:
                        continue
                logging.info("Ending Script For Today.")
                break
            elif dt.datetime.now() > pd.to_datetime(str(dt.datetime.now().date()) + " " + end_time):
                logging.info("Ending Script For Today.")
                show_notification(title="Ending!!!", message_text="Script For Automating ROLE is Ending For Today......")
                break
            else:
                print(f'\nCurrent Time : {dt.datetime.strftime(dt.datetime.now(), "%Y-%m-%d %I:%M:%S%p")}\n')
                print("This is no time for a class !!!\n")
                time.sleep(60)

        except Exception as err:
            logging.error(f"Error : {err} at main", stack_info=True)
            show_notification(title="Error Occurred!!!", message_text=err)
            continue


if __name__ == '__main__':
    while True:
        try:
            if dt.datetime.now() > pd.to_datetime(str(dt.datetime.now().date()) + " 10:16:00"):
                main()
            schedule.every().day.at("10:15").do(main)
            while True:
                schedule.run_pending()
        except:
            continue
