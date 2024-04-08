#!/usr/bin/python3

"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['54.146.65.66', '34.207.222.124']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:

# Distributes an archive to your web servers, using the function do_deploy


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    from fabric.api import env, put, run
    from os.path import exists
    env.hosts = ["100.25.118.136", "54.160.105.221"]

    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/" +
            archive_path[9:-4] + "/")
        run("tar -xzf /tmp/" + archive_path[9:] +
            " -C /data/web_static/releases/" +
            archive_path[9:-4] + "/")
        run("rm /tmp/" + archive_path[9:])
        run("mv /data/web_static/releases/" +
            archive_path[9:-4] + "/web_static/* /data/web_static/releases/" +
            archive_path[9:-4] + "/")
        run("rm -rf /data/web_static/releases/" +
            archive_path[9:-4] + "/web_static")
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/" +
            archive_path[9:-4] + "/ /data/web_static/current")
        return True
    except Exception:
        return False
