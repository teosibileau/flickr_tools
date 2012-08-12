from fabric.api import * 
import os
FAB_ROOT = os.path.dirname(os.path.realpath(__file__))

def virtualenv(command):
    if env.host_string is None or env.host_string is 'localhost':
        with lcd(env.directory):
            local("/bin/bash -l -c '%s && %s'"%(env.activate,command))
    else:
        with cd(env.directory):
            run("%s && %s"%(env.activate,command))

def push(message):
    if env.host_string is None or env.host_string is 'localhost':
        r=local
        c=lcd
    else:
        r=run
        c=cd
    with c(env.directory):
        r('git add . -A')
        r('git commit -m "%s"'%message)
        r('git push')

def pull():
    if env.host_string is None or env.host_string is 'localhost':
        with lcd(env.directory):
            local('git pull')
    else:
        with cd(env.directory):
            run('git pull')

def setup_virtualenv():
    if env.host_string is None or env.host_string is 'localhost':
        with lcd(env.directory):
            local('virtualenv . --distribute --no-site-packages')
    else:
        with cd(env.directory):
            run('virtualenv . --distribute --no-site-packages')

def install_requirements():
    virtualenv('pip install -r %s'%(os.path.join(FAB_ROOT,'requirements.txt')))
    
def setup_app():
    virtualenv('cd flickrtools && python manage.py syncdb --noinput')
    virtualenv('cd flickrtools && python manage.py migrate')

def freeze_env():
    virtualenv('pip freeze | grep -v distribute > requirements.txt')
    push('freezing enviroment requirements')

def update():
    install_requirements()
    setup_app()
    
def setup():
    setup_virtualenv()
    update()

def DEV():
    env.hosts=['localhost']
    env.directory=FAB_ROOT
    env.activate='source %s'%os.path.join(FAB_ROOT,'bin/activate')
