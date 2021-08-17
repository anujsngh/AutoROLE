import schedule
import time


def reading():
    print("Reading Time....")


def coding():
    print("Coding Time....")


def playing():
    print("Playing Time....")


if __name__ == '__main__':
    schedule.every(5).seconds.do(reading)
    schedule.every(10).seconds.do(coding)
    # schedule.every().day.at("19:49").do(playing)

    while True:
        schedule.run_pending()
        time.sleep(1)


