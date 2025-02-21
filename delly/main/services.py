from time import sleep
from django.core.mail import send_mail

def sleep_and_print(secs):
    sleep(secs)
    print('Task completed!')


def send_email(to):
    send_mail(
        subject="Links of the day!",
        message="Links of the day .. TODO! ",
        from_email="email@example.com",
        recipient_list=[to],
    )