#!/usr/bin/env python
from __future__ import absolute_import

from flaskext.script import Manager
from {{app.package_name}} import create_app

app = create_app()
manager = Manager(app)


if __name__ == "__main__":
    manager.run()
