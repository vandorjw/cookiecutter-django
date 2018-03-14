# gunicorn.py
bind = '0.0.0.0:5000'
backlog = 512
workers = 2
worker_class = 'gevent'
timeout = 60
