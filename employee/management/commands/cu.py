from django.core.management import BaseCommand

from employee.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=input('Введите вашу почту: '),
            is_active=True,
        )
        user.set_password(input('Введите ваш пароль: '))
        user.save()
