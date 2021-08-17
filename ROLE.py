import os
import time

import pandas as pd
import schedule
import datetime as dt
from bs4 import BeautifulSoup
from plyer import notification
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def show_notification(title=None, message_text=None):
    notification.notify(
            title=title,
            message=message_text,
            app_icon="1930264_check_complete_done_green_success_icon.ico",
            timeout=5,
            # app_name="app_name",
            # toast=True,
            # ticker="ticker"
        )


def do_login(driver=None, username=None, password=None):
    print("Logging In ......")
    # driver.get("https://cse.rgpvonline.org/calendar/view.php?view=upcoming")
    driver.get("https://cse.rgpvonline.org/calendar/view.php?view=day")
    driver.implicitly_wait(10)
    username_input = driver.find_element_by_xpath('//*[@id="username"]')
    password_input = driver.find_element_by_xpath('//*[@id="password"]')
    username_input.send_keys(username)
    password_input.send_keys(password)
    login_btn = driver.find_element_by_xpath('//*[@id="loginbtn"]')
    driver.find_element_by_xpath('//*[@id="rememberusername"]').click()
    login_btn.click()
    print("Successfully Logged In !!!")


def get_attendance_events(driver=None):

    event_soup = BeautifulSoup(driver.page_source, "lxml")

    div_list = event_soup.find_all("div")

    event_card_list = []
    for div in div_list:
        if div.has_attr("class"):
            if div["class"] == ["card", "rounded"]:
                parent_div = div.find_parent("div")
                if parent_div.has_attr("data-event-eventtype"):
                    if parent_div["data-event-eventtype"] == "attendance":
                        event_card_list.append(div)

    return event_card_list


def get_activity_links(event_card_list=None):
    activity_link_list = []
    for event_card in event_card_list:
        card_activity_link = event_card.find("a", {"class": "card-link"})["href"]
        activity_link_list.append(card_activity_link)

    return activity_link_list


def get_sub_activity_list(driver=None):
    sub_soup = BeautifulSoup(driver.page_source, "lxml")

    attendance_table = sub_soup.find("table", {"class": "generaltable"})

    attendance_df = pd.read_html(str(attendance_table))[0]

    status_ser = attendance_df["Status"][(attendance_df["Status"] != "Present") & (attendance_df["Status"] != "?")]

    status_link_list = []
    if not status_ser.empty:
        # status_link_list = sub_soup.find_all("a")
        status_link_list = driver.find_elements_by_link_text("Submit attendance")
        status_link_list = [i.get_attribute("href") for i in status_link_list]

    print()
    return status_link_list


def make_me_present(driver=None, status_link_list=None):
    sub_name = driver.find_element_by_css_selector("h1").text
    print(sub_name)
    print(status_link_list)
    if len(status_link_list):
        for status_link in status_link_list:
            driver.get(status_link)
            driver.implicitly_wait(10)

            try:

                radio_elems_labels = driver.find_elements_by_css_selector("label.form-check-inline")

                for radio_elem_label in radio_elems_labels:
                    span_text = radio_elem_label.find_element_by_css_selector("span.statusdesc").text
                    if span_text == "Present":
                        radio_input = radio_elem_label.find_element_by_css_selector("input.form-check-input")
                        radio_input.click()
                        driver.find_element_by_xpath('//*[@id="id_submitbutton"]').click()
                        driver.implicitly_wait(10)
                        show_notification(title="You Are Present Now !!!", message_text=sub_name)

            except Exception as exp:
                show_notification(title="Error Occurred!!!", message_text=exp)


def automate_attendance(cwdir_name=None, username=None, password=None):
    print("Starting Session ......")
    service = Service("/".join([cwdir_name, 'chromedriver']))
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
    print("Ending Session ......")


if __name__ == '__main__':
    while True:
        print(f'Current Time : {dt.datetime.strftime(dt.datetime.now(), "%Y-%m-%d %H:%M")}')
        if (dt.datetime.now() >= pd.to_datetime(str(dt.datetime.now().date()) + " 10:00:00")) and (dt.datetime.now() <= pd.to_datetime(str(dt.datetime.now().date()) + " 17:00:00")):
            cwd_name = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
            user_name = os.environ.get('ROLE_USERNAME')
            user_pass = os.environ.get('ROLE_PASSWORD')

            schedule.every(5).minutes.do(automate_attendance, cwdir_name=cwd_name, username=user_name, password=user_pass)

            automate_attendance(cwdir_name=cwd_name, username=user_name, password=user_pass)
            while True:
                schedule.run_pending()
        else:
            print("This is no time for a class !!!")
            time.sleep(60)
