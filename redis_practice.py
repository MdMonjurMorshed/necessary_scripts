"""Basic connection example.
"""

import redis

r = redis.Redis(
    host='redis-14736.c74.us-east-1-4.ec2.redns.redis-cloud.com',
    port=14736,
    decode_responses=True,
    username="default",
    password="<password>",
)

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)