from youjiao.extensions import db
from datetime import datetime
import sqlalchemy as sqla


class CRUDMixin(object):
    def __repr__(self):
        return "<{}>".format(self.__class__.__name__)

    def save(self):
        """Saves the object to the database."""
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        """Delete the object from the database."""
        db.session.delete(self)
        db.session.commit()
        return self

class CreateUpdateTimeMixin(object):
    create_time = db.Column(sqla.DateTime, default=datetime.utcnow)
    update_time = db.Column(sqla.DateTime, onupdate=datetime.utcnow)