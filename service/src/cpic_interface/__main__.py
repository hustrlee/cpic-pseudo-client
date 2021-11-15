#!/usr/bin/env python3
from cpic_interface.app import create_app


def main():
    app = create_app()
    app.add_api('openapi.yaml',
                arguments={'title': '广东太保医审平台案件交互接口'},
                pythonic_params=True)

    app.run(port=3001)


if __name__ == '__main__':
    main()
