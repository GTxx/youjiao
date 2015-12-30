from __future__ import absolute_import
import os
from flask import current_app
from youjiao.extensions import manager, flask_qiniu
import json
from qiniu import put_data


@manager.command
def create_qiniu_conf():
    static_dir = os.path.join(os.getcwd(), 'youjiao/static/build')
    print(os.getcwd())
    dest = "qiniu:access_key={}&secret_key={}&bucket={}&key_prefix={}".format(
        flask_qiniu.AK, flask_qiniu.SK, flask_qiniu.PUBLIC_BUCKET_NAME, flask_qiniu.STATIC_CDN_PREFIX)
    config = {"src": static_dir, "dest": dest, "debug_level": 1}
    with open('qiniu.json', 'w') as f:
        f.write(json.dumps(config))


@manager.command
def upload_static():
    import ipdb; ipdb.set_trace()
    STATIC_DIR = 'youjiao/static/build/'
    files = []
    for prefix, _dir, file_list in os.walk(STATIC_DIR):
        for file_name in file_list:
            files.append(os.path.join(prefix, file_name))

    bucket_name = current_app.qiniu.PUBLIC_BUCKET_NAME
    for file in files:
        with open(file) as f:
            _prefix, key = file.split(STATIC_DIR)
            print('upload {}'.format(os.path.join('static', key)))
            key = os.path.join('static', key)
            up_token = flask_qiniu.qiniu_auth.upload_token(bucket_name, key,
                                                           policy={})
            res = put_data(up_token=up_token, key=key, data=f.read())


@manager.command
def build_static():
    current_path = os.getcwd()
    static_path = os.path.join(current_path, 'youjiao/static')
    os.chdir(static_path)
    os.system('npm run build-product')
