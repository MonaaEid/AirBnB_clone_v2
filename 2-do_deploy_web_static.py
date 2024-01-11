#!/usr/bin/python3
"""python script"""
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['54.90.1.129', '18.208.119.233']


def do_deploy(archive_path):
    """deploy the archived code"""
    if not exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")

        archive_filename = archive_path.split("/")[-1]
        archive_name_no_ext = archive_filename.split(".")[0]
        run("sudo mkdir -p /data/web_static/releases/{}/".format(archive_name_no_ext))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            archive_filename, archive_name_no_ext))

        run("sudo rm /tmp/{}".format(archive_filename))

        run("sudo rm -f /data/web_static/current")

        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current".format(archive_name_no_ext))

        return True

    except Exception:
        return False
