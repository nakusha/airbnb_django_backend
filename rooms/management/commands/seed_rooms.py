import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    help = "Add Amenities automatically"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many rooms you wnat to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_usser = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()

        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_usser),
                "room_type": lambda x: random.choice(room_types),
                "price": lambda x: random.randint(10000, 30000),
                "guests": lambda x: random.randint(1, 5),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(5, 10)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"/room_photos/{random.randint(1,13)}.jpeg",
                )
            for a in amenities:
                magic_number = random.randint(0, 10)
                if magic_number % 2 == 0:
                    room.amenities.add(a)

            for f in facilities:
                magic_number = random.randint(0, 10)
                if magic_number % 4 == 0:
                    room.facilities.add(f)

            for r in rules:
                magic_number = random.randint(0, 10)
                if magic_number % 3 == 0:
                    room.house_rule.add(r)
        self.stdout.write(self.style.SUCCESS(f"{number} Rooms Created success"))
