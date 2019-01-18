from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail

import dramatiq

from spirit.topic.models import Topic


@dramatiq.actor
def notify_comment(user_id, topic_id):
    subject = "Respondieron a un tema en el que estás suscripto"
    return notify_by_mail(user_id, topic_id, subject)


@dramatiq.actor
def notify_mention(user_id, topic_id):
    subject = "Te mencionaron un tema"
    return notify_by_mail(user_id, topic_id, subject)


def notify_by_mail(user_id, topic_id, subject):
    # TODO: Poner tries
    user = User.objects.get(pk=user_id)
    topic = Topic.objects.get(pk=topic_id)

    msg = 'entrá en {}{}'.format(
        settings.SITE_URL,
        topic.get_absolute_url()
    )

    send_mail(
        subject,
        msg,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=True,
    )
