#!/usr/bin/env python3
import connexion

from cpic_interface import encoder
from cpic_interface.db_config import init_db


def main():

    connex_app = connexion.App(__name__, specification_dir="./openapi/")

    connex_app.app.json_encoder = encoder.JSONEncoder
    connex_app.add_api('openapi.yaml',
                       arguments={'title': '广东太保医审平台案件交互接口'},
                       pythonic_params=True)

    connex_app.app.app_context().push()
    init_db(connex_app.app)

    connex_app.run(port=3001)


if __name__ == '__main__':
    main()
