import os
from youjiao.extensions import manager, qiniu
import json


@manager.command
def create_qiniu_conf():
    static_dir = os.path.join(os.getcwd(), 'static/uild')
    dest = "qiniu:access_key={}&secret_key={}&bucket={}&key_prefix={}".format(
        qiniu.AK, qiniu.SK, qiniu.PUBLIC_BUCKET_NAME, qiniu.STATIC_CDN_PREFIX)
    config = {"src": static_dir, "dest": dest, "debug_level": 1}
    with open('qiniu.json', 'w') as f:
        f.write(json.dumps(config))
