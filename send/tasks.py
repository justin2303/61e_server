from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_async_email(subject, message, recips):
    # Replace 'your_email@gmail.com', 'your_password' with your email credentials

    try:
        send_mail(
            subject,
            message,
            from_email=None,
            recipient_list=recips,
        )
        return "Email sent successfully."
    except Exception as e:
        return f"Email sending failed: {str(e)}"