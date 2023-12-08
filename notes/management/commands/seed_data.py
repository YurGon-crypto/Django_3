from django.core.management.base import BaseCommand
from notes.models import Category, Note
from django.utils import timezone

class Command(BaseCommand):
    help = 'Seed the database with test data'

    def handle(self, *args, **kwargs):
        category1 = Category.objects.create(title='Personal')
        category2 = Category.objects.create(title='Work')

        Note.objects.create(title='Meeting', text='Team meeting at 3 PM', reminder=timezone.now(), category=category2)
        Note.objects.create(title='Groceries', text='Buy milk and eggs', category=category1)
        Note.objects.create(title='Gym', text='Workout at 6 AM', reminder=timezone.now(), category=category1)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))
