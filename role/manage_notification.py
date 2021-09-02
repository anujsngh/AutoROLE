from role import logging, notification


def show_notification(title=None, message_text=None):
    logging.info(title + " " + message_text)
    notification.notify(
            title=title,
            message=message_text,
            app_icon="resources/green_tick.ico",
            timeout=5,
            app_name="Automate_ROLE",
            # toast=True,
            # ticker="ticker"
        )


if __name__ == '__main__':
    show_notification(title="test", message_text="test text")
