from app.database import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    nickname = db.Column(db.Unicode(), unique=True)
