import os, random, sys, django
from faker import Faker


back = os.path.dirname
BASE_DIR = back(back(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
url_file_path = 'E:/workspace/web_spiders/baiduimage'


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "max.settings")
    django.setup()
    fake = Faker('zh_CN')


    from contests.models import Team
    team_lenth = 0
    print('清空数据库Team对象...')
    Team.objects.all().delete()
    url_path = os.path.join(url_file_path, 'team.txt')
    f = open(url_path, encoding='utf-8')
    for line in f.readlines():
        team_lenth += 1
        team = Team.objects.create(
            name=str(random.randint(1000,9999))+fake.company(),
            logo=line.strip('\n'))
        team.save()
    print('Team对象数据创建完成')


    from contests.models import Contests
    contests_lenth = 0
    print('清空数据库Contests对象...')
    Contests.objects.all().delete()
    for i in range(0, 5):
        contests_lenth += 1
        contests = Contests.objects.create(
            contests_name=fake.sentence().strip('.'),
            is_end=fake.boolean(chance_of_getting_true=50))
        contests.save()
    print('Contests对象数据创建完成')


    from contests.models import Game
    game_length = 0
    print('清空数据库Game对象...')
    Game.objects.all().delete()
    for i in range(0, team_lenth*5):
        game_length += 1
        r_index = random.randint(0, team_lenth-1)
        if r_index == 0 or r_index == team_lenth-1:
            b_index = random.randint(1, team_lenth-2)
        else:
            l1 = list(range(0,r_index))
            l2 = list(range(r_index+1, team_lenth))
            l1.extend(l2)
            b_index = random.choice(l1)
        game = Game.objects.create(
            is_end=fake.boolean(chance_of_getting_true=50),
            game_status=random.randint(0, 2),
            contests=Contests.objects.all()[random.randint(0, contests_lenth-1)],
            r_team=Team.objects.all()[r_index],
            b_team=Team.objects.all()[b_index])
        game.save()
    print('Game对象数据创建完成')


    from contests.models import Commentary
    print('清空数据Commentary对象...')
    Commentary.objects.all().delete()
    for i in range(0, game_length*5):
        commentary = Commentary.objects.create(
            time=fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None),
            story=fake.text(max_nb_chars=random.randint(100, 200)),
            game=Game.objects.all()[random.randint(0, game_length-1)])
        commentary.save()
    print('Commentary对象数据创建完成')


    from user.models import User
    user_length = 0
    print('清空数据库User对象...')
    User.objects.all().delete()
    url_path = os.path.join(url_file_path, 'user.txt')
    f = open(url_path, encoding='utf-8')
    for line in f.readlines():
        user_length += 1
        user = User.objects.create(
            name=fake.ean13(),
            password=fake.password(length=random.randint(8, 25)),
            nickname=fake.name(),
            email=fake.ean8()+fake.email(),
            sex=random.randint(0,1),
            is_activated=True,
            portrait=line.strip('\n'),
            team=Team.objects.all()[random.randint(0, team_lenth-1)])
        user.save()
    print('User对象数据创建完成')


    from news.models import News
    print('清空数据库News对象...')
    News.objects.all().delete()
    url_path = os.path.join(url_file_path, 'news.txt')
    f = open(url_path, encoding='utf-8')
    for line in f.readlines():
        news = News.objects.create(
            author = User.objects.all()[random.randint(0, user_length-1)],
            title = fake.sentence().strip('.'),
            text = fake.text(random.randint(500, 1000)),
            views = random.randint(0, 100000),
            cover_url = line.strip('\n'),
            released_time=fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None))
        news.save()
    print('News对象数据创建完成')