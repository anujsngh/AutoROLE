from role import logging, notification, cwdir_name


def show_notification(title=None, message_text=None):
    pass
    # logging.info(str(title) + " " + str(message_text))
    # notification.notify(
    #         title=title,
    #         message=message_text,
    #         app_icon="/".join([cwdir_name, "resources/green_tick.ico"]),
    #         timeout=5,
    #         app_name="Automate_ROLE",
    #         # toast=True,
    #         # ticker="ticker"
    #     )


if __name__ == '__main__':
    show_notification("Test", "Test Text")
