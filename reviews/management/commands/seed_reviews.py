import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews import models as review_models
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    help = "Add Reviews automatically"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many reivews you wnat to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        rooms = room_models.Room.objects.all()
        users = user_models.User.objects.all()
        seeder.add_entity(
            review_models.Review,
            number,
            {
                "accuracy": lambda x: random.randint(0, 5),
                "communcation": lambda x: random.randint(0, 5),
                "cleanlines": lambda x: random.randint(0, 5),
                "location": lambda x: random.randint(0, 5),
                "check_in": lambda x: random.randint(0, 5),
                "value": lambda x: random.randint(0, 5),
                "room": lambda x: random.choice(rooms),
                "user": lambda x: random.choice(users),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} of reviews created"))
