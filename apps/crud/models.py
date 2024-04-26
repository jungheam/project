from apps.app import db


class User(db.Model):
    __tablename__ = "toyrental"
    number = db.Column(db.Integer, primary_key=True) #번호
    toyname = db.Column(db.String) #장난감이름
    age = db.Column(db.Integer) #연령
    components = db.Column(db.String, unique=True) #구성품
    explain = db.Column(db.String) #설명
    rental = db.Column(db.Boolean) #렌탈여부
