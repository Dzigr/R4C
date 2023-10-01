from django.conf import settings
from django.core.mail import send_mail


class EmailService:
    @classmethod
    def send_email_to_customers(cls, robot, customers):
        subject = f"Robot with serial {robot} is available"
        message = (
            f"Добрый день!\n"
            f"Недавно вы интересовались нашим роботом "
            f"модели {robot.model}, версии {robot.version}.\n"
            f"Этот робот теперь в наличии. "
            f"Если вам подходит этот вариант - пожалуйста, свяжитесь с нами."
        )
        send_mail(
            subject,
            message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=customers,
        )
