from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "This Command tells me hello"

    def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="how many times do you want to tell you hello"
        )
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        times = options.get("times")

        for t in range(0, int(times)):
            self.stdout.write(self.style.SUCCESS("hello"))
