import os

from django.core.management import BaseCommand

from employee.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('EMAIL'),
            first_name=os.getenv('FIRST_NAME'),
            is_staff=True,
            is_active=True,
            is_superuser=True,
        )
        user.set_password(os.getenv('PASSWORD'))
        user.save()
