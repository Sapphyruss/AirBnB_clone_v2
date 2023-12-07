#!/usr/bin/python3
"""distribute an archive to the web servers"""
from os.path import exists
from fabric.api import env, run, put, task

env.hosts = ["100.25.110.120", "34.207.178.181"]
env.user = "ubuntu"
# archive_path = "versions/web_static_20231004205451.tgz"


@task
def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if not exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        archive = archive_path.split("/")[1]
        file = archive.split(".")[0]
        release = "/data/web_static/releases/"
        folder = "/data/web_static/releases/{}".format(file)
        run("mkdir -p {}".format(folder))
        run(" tar -xzf /tmp/{} -C {}".format(archive, folder))
        run("rm /tmp/{}".format(archive))
        run("mv {}{}/web_static/* {}{}/".format(release, file, release, file))
        run("rm -rf /data/web_static/releases/{}/web_static".format(file))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder))
        print("New version deployed!")
        return True
    except Exception:
        return False
