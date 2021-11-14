#!/usr/bin/env python3

import connexion

from cpic_interface import encoder


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': '广东太保医审平台案件交互接口'},
                pythonic_params=True)

    app.run(port=3001)


if __name__ == '__main__':
    main()
