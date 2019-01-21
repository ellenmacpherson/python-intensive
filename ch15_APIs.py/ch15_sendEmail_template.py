import requests


def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/YOUR_MAILGUN_URL/messages",
        auth=("api", "API_HERE"),
        data={"from": "Excited User <mailgun@YOUR_MAILGUN_URL>",
              "to": ["EMAIL_HERE", "YOUR_MAILGUN_URL"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomeness!"})

send_simple_message()
