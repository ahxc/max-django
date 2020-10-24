# 这是一个删除sqlite3数据库，清空应用下migration迁移文件和缓存文件的脚本

import shutil, os, sys


back = os.path.dirname
roots = back(back(os.path.abspath(__file__)))


l = ['contests', 'news', 'user']


p1 = os.path.join(roots, 'db.sqlite3')
try:
        os.remove(p1)
except:
    print(p1+'，不存在')


for i in l:
    pi = os.path.join(roots, i)
    p2 = os.path.join(pi, '__pycache__')
    p3 = os.path.join(pi, 'migrations')
    p4 = os.path.join(p3, '__init__.py')
    try:
        shutil.rmtree(p2)
    except:
        print(p2+'，不存在')
    try:
        shutil.rmtree(p3)
    except:
        print(p3+'，不存在')
    os.mkdir(p3)
    with open(p4, 'a', encoding="utf-8") as f:
        f.write('# -*- coding:utf-8 -*-')
        f.close()
    print('已完成{}目录下迁移文件和缓存文件的删除，并建立了{}/migrations/__init__.py'.format(i,i))