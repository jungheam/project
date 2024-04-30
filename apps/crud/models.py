from apps.app import db, login_manager
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = "toyrental"
    number = db.Column(db.Integer, primary_key=True) #번호
    toyname = db.Column(db.String) #장난감이름
    age = db.Column(db.Integer) #연령
    type = db.Column(db.String) #유형별
    components = db.Column(db.String) #구성품
    explain = db.Column(db.String) #설명
    rental = db.Column(db.String) #렌탈여부

    def get_id(self):
           return (self.number)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
