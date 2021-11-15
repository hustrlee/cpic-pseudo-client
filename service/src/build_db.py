import os
import connexion

from cpic_interface.db_config import init_db, db
from cpic_interface.db_models import Customer
import cpic_interface


def main():
    connex_app = connexion.App(__name__, specification_dir="./openapi/")
    init_db(connex_app.app)

    # 如果数据库文件存在，则删除它
    basedir = os.path.dirname(cpic_interface.__file__)
    database_file = os.path.join(basedir, "cpic.db")
    if os.path.exists(database_file):
        os.remove(database_file)

    # 创建数据库
    db.create_all()

    # 插入记录
    gdtb = Customer("21", "广东太保", "gdtb", "asdfghjkl", "dwsuhfci")
    db.session.add(gdtb)
    db.session.commit()


if __name__ == '__main__':
    main()
