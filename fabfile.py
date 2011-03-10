def hello():
    print("Hello world!")
    
from fabric.api import local

def prepare_deploy():
    local("./manage.py migrate")
    local("hg commit -m 'yo'")  