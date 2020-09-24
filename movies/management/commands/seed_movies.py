from random import choice, randint
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten

from django_seed import Seed
from movies.models import Movie
from categories.models import Category
from people.models import Person


class Command(BaseCommand):

    help = "This command seeds movies"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            help="How many movies do you want to create?",
            default=10)

    def handle(self, *args, **options):
        total = int(options.get('total'))
        categories = Category.objects.all()
        directors = Person.objects.filter(kind=Person.KIND_DIRECTOR)
        seeder = Seed.seeder()
        seeder.add_entity(
            Movie, total, {
                "year": lambda x: seeder.faker.year(),
                "rating": lambda x: randint(1, 5),
                "category": lambda x: choice(categories),
                "cover_image": lambda x: f"/moviecover/_{randint(1,20)}.jpeg",
                "director": lambda x: choice(directors),
            })
        model = seeder.execute()
        lists = flatten(list(model.values()))

        for pk in lists:
          model = Movie.objects.get(pk=pk)

          for person in Person.objects.all():
            if randint(1,100)%2 and person.kind==Person.KIND_ACTOR:
              model.cast.add(person)

        self.stdout.write(self.style.SUCCESS(f'{total} movies created!'))

