from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    custid = db.Column(db.String(50))
    salt = db.Column(db.String(50))
    appkey = db.Column(db.String(50))
    secrectkey = db.Column(db.String(50))

    def __init__(self, name, custid, salt, appkey, secrectkey):
        self.name = name
        self.custid = custid
        self.salt = salt
        self.appkey = appkey
        self.secrectkey = secrectkey

    def __repr__(self) -> str:
        return "客户名：%r" % self.name
