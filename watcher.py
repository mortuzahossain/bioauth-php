from settings import *
import json

# Initializing our database
db = SQLAlchemy(app)
class Watcher(db.Model):
    __tablename__ = 'watcher'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=True)
    isNewUserRegistered = db.Column(db.Integer, nullable=False)

    def json(self):
        return {'id': self.id, 'isNewUserRegistered': self.isNewUserRegistered}

    def add_new(_isNewUserRegistered):
        new_user = Watcher(username="Hello",isNewUserRegistered=_isNewUserRegistered)
        db.session.add(new_user)
        db.session.commit()

    def update_user(_id, _isNewUserRegistered):
        user_to_update = Watcher.query.filter_by(id=_id).first()
        user_to_update.isNewUserRegistered = _isNewUserRegistered
        db.session.commit()