#!/usr/bin/python3
"""this module creates a tar archive"""

from fabric.api import local
import os.path
import datetime


def do_pack():
    """creates a tar archive from the static files"""
    if not os.path.isdir("./versions"):
        local("mkdir versions")

    x = datetime.datetime.now()
    file_tar = "web_static_{}{}{}{}{}{}.tgz".format(
        x.year, x.month, x.day, x.hour, x.minute, x.second)

    result = local("tar -cvzf versions/{} web_static".format(file_tar))

    if result.succeeded:
        return "./versions{}".format(file_tar)
    else:
        return None
