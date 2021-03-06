import aioredis
import os
import json
from network import broadcast

async def consume_redis_queue():
    redis_host = os.getenv("REDIS_HOST")
    redis_password = os.getenv("REDIS_PASSWORD")

    if redis_host == None or redis_password == None:
        raise Exception("Missing redis configuration variables")

    r = await aioredis.create_redis_pool(redis_host, password = redis_password)
    while True:
        itemEncoded = await r.brpop('notifications:queue')
        item = json.loads(itemEncoded[1].decode('utf-8'))
        await broadcast(item)

