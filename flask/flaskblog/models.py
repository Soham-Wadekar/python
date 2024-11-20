import datetime
from itsdangerous import Serializer, TimestampSigner

from flask import current_app
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    img_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    def get_reset_token(self):
        s = Serializer(current_app.secret_key)
        signer = TimestampSigner(current_app.secret_key)
        return signer.sign(s.dumps({"user_id": self.id})).decode("utf-8")

    @staticmethod
    def verify_reset_token(token, expires_in=1800):
        s = Serializer(current_app.secret_key)
        signer = TimestampSigner(current_app.secret_key)

        try:
            unsigned_token = signer.unsign(token.encode("utf-8"), max_age=expires_in)
            user_id = s.loads(unsigned_token)["user_id"]
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.img_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(
        db.String(100),
        nullable=False,
        default=str(
            datetime.datetime.now(datetime.timezone.utc).strftime("%d %b %Y %H:%M")
        ),
    )
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
