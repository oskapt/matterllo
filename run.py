# -*- coding: utf-8 -*-
"""
    matterllo.run
    ~~~~~~~~~~~~~

    A simple endpooint to run the web application.

    :copyright: (c) 2016 by Lujeni.
    :license: BSD, see LICENSE for more details.
"""
import os

from matterllo import app


def main():
    try:
        debug = os.environ.get("MATTERLLO_API_DEBUG", False)
        host = os.environ.get("MATTERLLO_API_HOST", 'localhost')
        port = os.environ.get("MATTERLLO_API_PORT", 8080)
        app.run(host=host, port=port, debug=debug)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == '__main__':
    main()
