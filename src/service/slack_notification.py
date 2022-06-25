from slack import WebClient  # not written webclient


def send_slack_notification():
    client = WebClient(token="")

    response = client.chat_postMessage(
        channel="",
        text=""
    )
