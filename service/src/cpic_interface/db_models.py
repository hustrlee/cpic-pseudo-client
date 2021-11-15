from cpic_interface.db_config import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    custid = db.Column(db.String(50))
    name = db.Column(db.String(50))
    salt = db.Column(db.String(50))
    appkey = db.Column(db.String(50))
    secrectkey = db.Column(db.String(50))

    def __init__(self, custid=None, name=None, salt=None, appkey=None, secrectkey=None):
        self.custid = custid
        self.name = name
        self.salt = salt
        self.appkey = appkey
        self.secrectkey = secrectkey

    def __repr__(self) -> str:
        return "客户名：%r" % self.name

    def to_dict(self) -> dict:
        # dictret = dict(self.__dict__)
        # dictret.pop('_sa_instance_state', None)

        # return dictret
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
