from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import Message
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=Message)
def send_email_on_message_creation(sender, instance, created, **kwargs):
    if created:
        subject = f"Proftolio Website New Message | {instance.name}"
        body = f"Name: {instance.name}\nEmail: {instance.email}\nMessage:\n{instance.message}"
        recipient = "ksourmi@gmail.com"

        send_mail(
            subject=subject,
            message=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient],
            fail_silently=False,
        )