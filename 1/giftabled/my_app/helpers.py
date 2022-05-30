from django.core.email import send_mail
import uuid
from django.conf import settings

def send_forget_password_mail(email):
    token=str(uuid.uuid4())
    subject='Password Reset Link'
    message='Hi, Click here to reset your password http://127.0.0.1:8000/reset/'+token+'/'
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list)
    return True