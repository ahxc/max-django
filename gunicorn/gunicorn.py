# -*- coding: UTF-8 -*-


workers=3   

threads = 3 

bind=['192.168.3.82:8000']

proc_name='max'   

accesslog = './gunicorn/log/acess.log'
errorlog = './gunicorn/log/error.log'

# pidfile='/tmp/blog.pid'   

# worker_class='gevent'

# timeout=30

# max_requests=6000