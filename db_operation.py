import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weborm.settings")
django.setup()

from weborm.models import Greeting

# Create an author
author = Greeting(message='Hello world').save()



# Query books by author
books_by_author = Greeting.objects.all()

print(books_by_author)
