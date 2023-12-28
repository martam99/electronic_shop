from django.contrib.auth.models import Group
from django.core.management import BaseCommand

from employee.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=input('Введите вашу почту: '),
            is_active=True,
            is_staff=True,
        )
        user.set_password(input('Введите ваш пароль: '))
        user.save()
        active_employee = Group.objects.get(name='Active_employee')
        active_employee.user_set.add(user)
