from cpic_interface.db_config import db
from sqlalchemy import JSON


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    custid = db.Column(db.String(50))
    name = db.Column(db.String(50))
    salt = db.Column(db.String(50))
    appkey = db.Column(db.String(50))
    secretkey = db.Column(db.String(50))

    def __init__(self, custid=None, name=None, salt=None, appkey=None, secretkey=None):
        self.custid = custid
        self.name = name
        self.salt = salt
        self.appkey = appkey
        self.secretkey = secretkey

    def __repr__(self) -> str:
        return "客户名：%r" % self.name

    def to_dict(self) -> dict:
        # 第一种实现方法
        # dictret = dict(self.__dict__)
        # dictret.pop('_sa_instance_state', None)

        # return dictret
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


class Case(db.Model):
    case_no = db.Column(db.String(50), primary_key=True, autoincrement=False)
    uuid = db.Column(db.String(50))
    appkey = db.Column(db.String(50))
    insure_code = db.Column(db.String(20))
    insure_name = db.Column(db.String(50))
    regist_no = db.Column(db.String(50))
    sign = db.Column(db.String(50))
    timestamp = db.Column(db.String(50))
    weight = db.Column(db.Integer)
    zmark = db.Column(db.String(255))
    images = db.Column(JSON)

    def __init__(
        self,
        case_no=None,
        uuid=None,
        appkey=None,
        insure_code=None,
        insure_name=None,
        regist_no=None,
        sign=None,
        timestamp=None,
        weight=None,
        zmark=None,
        images=None
    ):
        self.case_no = case_no
        self.uuid = uuid
        self.appkey = appkey
        self.insure_code = insure_code
        self.insure_name = insure_name
        self.regist_no = regist_no
        self.sign = sign
        self.timestamp = timestamp
        self.weight = weight
        self.zmark = zmark
        self.images = images

    def to_dict(self) -> dict:
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
