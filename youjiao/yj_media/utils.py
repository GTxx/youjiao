from flask import current_app
from urlparse import urljoin

q = current_app.qiniu.qiniu_auth

def get_private_url(key):
    PRIVATE_DOMAIN = current_app.qiniu.PRIVATE_CDN_DOMAIN
    url = urljoin(PRIVATE_DOMAIN, key)
    return q.private_download_url(url, expires=3600)

