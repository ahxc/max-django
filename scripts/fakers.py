import os, random, sys, django
from faker import Faker
from datetime import timedelta
from django.utils import timezone


back = os.path.dirname
BASE_DIR = back(back(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
url_file_path = 'E:/workspace/web_spiders/baiduimage'


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "max.settings")
    django.setup()
    fake = Faker('zh_CN')


    from news.models import News
    print('清空数据库News对象')
    News.objects.all().delete()
    url_path = os.path.join(url_file_path, 'news.txt')
    f = open(url_path, encoding='utf-8')
    for line in f.readlines():
        news = News.objects.create(
            title = fake.sentence().strip('.'),
            text = '\n\n'.join(fake.paragraphs(10)),
            views = random.randint(0, 100000),
            cover_url = line)
        news.save()
    print('News对象数据创建完成')


    from contests.models import Team
    team_lenth = 0
    print('清空数据库Team对象')
    Team.objects.all().delete()
    url_path = os.path.join(url_file_path, 'team.txt')
    f = open(url_path, encoding='utf-8')
    for line in f.readlines():
        team_lenth += 1
        team = Team.objects.create(
            name=str(random.randint(1000,9999))+fake.company(),
            logo=line)
        team.save()
    print('Team对象数据创建完成')


    from contests.models import Contests
    contests_lenth = 0
    print('清空数据库Contests对象')
    Contests.objects.all().delete()
    for i in range(0, 5):
        contests_lenth += 1
        contests = Contests.objects.create(
            contests_name=fake.sentence().strip('.'),
            is_end=fake.boolean(chance_of_getting_true=50))
        contests.save()
    print('Team对象数据创建完成')


    from contests.models import Game
    print('清空数据库Contests对象')
    Game.objects.all().delete()
    for i in range(0, 5):
        game = Game.objects.create(
            is_end=fake.boolean(chance_of_getting_true=50),
            choices=random.randint(0, 2),
            contests=Contests.objects.all()[random.randint(0, contests_lenth-1)],
            r_team=Team.objects.all()[random.randint(0, team_lenth-1)],
            b_team=Team.objects.all()[random.randint(0, team_lenth-1)])
        game.save()
    print('Team对象数据创建完成')


    from user.models import User
    print('清空数据库User对象')
    User.objects.all().delete()
    url_path = os.path.join(url_file_path, 'user.txt')
    f = open(url_path, encoding='utf-8')
    for line in f.readlines():
        user = User.objects.create(
            name=fake.ean13(),
            password=fake.password(length=random.randint(8, 25)),
            nickname=fake.name(),
            email=fake.ean8()+fake.email(),
            sex=random.randint(0,1),
            is_activated=True,
            portrait=line,
            team=Team.objects.all()[random.randint(0, team_lenth-1)])
        user.save()
    print('User对象数据创建完成')