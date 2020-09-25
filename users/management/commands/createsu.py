from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = "This command will make super user."

    def handle(self, *args, **options):

        try:
            ebadmin = User.objects.get(username="ebadmin")        
            self.stdout.write(self.style.ERROR(f"Superuser already existed"))
        except User.DoesNotExist:
            User.objects.create_superuser(
                "ebadmin", "pleed0215@gmail.com", "adminadmin1!")
            self.stdout.write(
                self.style.SUCCESS(
                    f"Superuser created"
                )
            )

