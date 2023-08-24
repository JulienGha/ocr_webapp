# worker.py
import redis
from rq import Worker, Queue, Connection

listen = ['default']

redis_url = 'redis://redis:6379'  # Note the change from localhost to service name

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(Queue))
        worker.work()
