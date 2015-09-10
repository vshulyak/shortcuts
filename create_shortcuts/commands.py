import sys
import subprocess

args_joined = lambda: " ".join(sys.argv[1:])

"""
Hold on, Hold on!

Yes, executing commands below using python seem to be weird. Even awkward.

But! It's supereasy to bootstrap a project using buildout.

"""


def build():
    subprocess.call("./bin/docker-compose build", shell=True)


def up():
    subprocess.call("./bin/docker-compose up", shell=True)


def django():
    subprocess.call("docker exec -it $(./bin/docker-compose ps | grep web "
                    "| awk '{print $1}') ./bin/django %s" % args_joined(),
                    shell=True)


def djsh():
    subprocess.call("docker exec -it $(./bin/docker-compose ps | grep web | awk '{print $1}') ./bin/django shell_plus",
                    shell=True)


def djtest():
    subprocess.call("docker exec -it $(./bin/docker-compose ps | grep web | awk '{print $1}') "
                    "./bin/django test --settings=settings --configuration=Test %s" % args_joined(),
                    shell=True)


def flake8():
    subprocess.call("docker exec -it $(./bin/docker-compose ps | grep web "
                    "| awk '{print $1}') ./bin/flake8 %s" % args_joined(), shell=True)


def killcelery():
    subprocess.call("docker exec -it $(./bin/docker-compose ps | grep worker "
                    "| awk '{print $1}') killall celery", shell=True)


def runsp():
    subprocess.call("./bin/docker-compose run --service-ports %s" % args_joined(), shell=True)


def sh():
    subprocess.call("docker exec -it $(./bin/docker-compose ps | grep $1 | awk '{print $1}') bash",
                    shell=True)


def stop():
    subprocess.call("./bin/docker-compose stop",
                    shell=True)