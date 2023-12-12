from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='test2@testov.ru',
            first_name='Test',
            last_name='Testov',
            is_staff=False,
            is_superuser=False,
            login_as=True,
        )

        user.set_password('123qweqwe')
        user.save()