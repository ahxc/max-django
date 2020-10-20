import os, pathlib, random, sys, django
from faker import Faker

from datetime import timedelta
from django.utils import timezone

back = os.path.dirname

BASE_DIR = back(back(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

if __name__ == '__main__':
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "max.settings")
  
  django.setup()

  from news.models import News

  print('清空数据库')
  News.objects.all().delete()

  fake = Faker()
  for _ in range(50):
    news = News.objects.create(
      title = fake.sentence().rstrip('.'),
      body = '\n\n'.join(fake.paragraphs(10)),
    )
    news.save()

  fake = Faker('zh_CN')
  for _ in range(50):
    news = News.objects.create(
      title = fake.sentence().rstrip('.'),
      body = '\n\n'.join(fake.paragraphs(10)),
    )
    news.save()