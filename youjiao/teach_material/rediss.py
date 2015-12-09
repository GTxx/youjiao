__author__ = 'yt'

from models import Courseware
from ..extensions import redis_cli

class RedisClick(object):
    for id in Courseware.id:
        courseware = Courseware.query.get(id)
        redis_cli.set(courseware.name, "visit%s" % id)


