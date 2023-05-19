from typing import OrderedDict
from django.core.management.base import BaseCommand
from authentication.models import Company, Profession
from main.utils import CITIES, SHORT_CITIES
from faker import Faker
# import faker.providers
from django.utils.text import slugify
from main.models import Job, Skill


class Provider():
    def main_jobs(self, col, fake, swrite, style):
        swrite.write(style.SUCCESS("\nSTARTED GENERATING Jobs\n"))
        company = Company.objects.get(id=2)
        for i in range(int(col)):
            i += 1
            text = fake.job()
            swrite.write(style.WARNING(f"\n{i}. Start creating"))
            print(f">> '{text}'")
            slug = slugify(text)
            profession = Profession.objects.get(
                id=fake.random_int(min=1, max=4))
            description = fake.text(max_nb_chars=2000)
            salary = fake.random_int()
            city = fake.random_choices(elements=SHORT_CITIES, length=1)
            skills = fake.text(max_nb_chars=200)
            job = Job.objects.create(name=text, slug=slug, description=description, company=company,
                                     profession=profession, salary=salary, skills=skills, city=city)
            print("UNTIL HERE OK")
            job.save()
            swrite.write(style.SUCCESS(f"\n{i}. Created"))
            print(f">> '{text}'")
        check_items = Job.objects.all().count()
        swrite.write(style.SUCCESS(f"\nNumber of items: {check_items}"))


text = """
==============================================
=                      Hello!
= What do you want to generate >

= 1. Jobs

= (choose a number)
==============================================
            """

# calm


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        fake = Faker(['en_US'])
        swrite = self.stdout
        style = self.style

        while True:
            select = input(text)
            if int(select) == 1:
                col_items = input("How many jobs do you want to generate >>>")

                if col_items.isnumeric():
                    Provider.main_jobs(self, col=col_items,
                                       fake=fake, swrite=swrite, style=style)

                else:
                    self.stdout.write(self.style.ERROR("Not correct"))
            else:
                print("Bye")
                break
