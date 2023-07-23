from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.conf import settings

from .models import Post, PostCategory




def send_notifications(preview, pk, title, subscribers):
    html_contect = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/posts/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_contect, 'text/html')
    msg.send()

@receiver(post_save, sender=Post)
def post_created(instance, **kwargs):
    print('Создана статья', instance)


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers += category.subscribers.all()

        subscribers += [s.email for s in subscribers]
        print(subscribers)

        send_notifications(instance.preview(), instance.pk, instance.title, subscribers)
#


# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from .models import Post
# from .tasks import *
#
# from django.contrib.auth.models import User
# from django.core.mail import EmailMultiAlternatives
#
#
# @receiver(post_save, sender=Post)  # декоратор для сигналов
# def post_created(sender, instance, created, **kwargs):
#     """Сигнал срабатывает при появлении новой публикации и вызывает таску"""
#     if created:  # при появлении новой публикации
#         # получаем email подписчиков этой публикации
#         emails = list(User.objects.filter(subscribers__category=instance.category).values_list('email', flat=True))
#
#         # вызываем нашу таску и передаем ей необходимые аргументы
#         with_every_new_post.delay(instance.category.title,
#                                   instance.preview(),
#                                   instance.title,
#                                   emails,
#                                   instance.get_absolute_url(),
#                                   )





