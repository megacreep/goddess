from fabric.api import *
from fabric.contrib.files import exists

REPOS = (("https://github.com/megacreep/goddess.git", "origin", "master"),)

env.user = 'ubuntu'
env.key_filename = ['temp.pem']
env.hosts = ['yutianxin.me']


@hosts(['yutianxin.me'])
def deploy():
    if not exists('/var/www/goddess'):
        run('mkdir -p /var/www/goddess')

    with cd('/var/www/goddess'):
        run('git reset --hard')
        run('git pull')
        run('python manage.py collectstatic --noinput')
        # Migrate and Update the database
        run('python manage.py makemigrations')
        run('python manage.py migrate')
        run('python manage.py syncdb')

    # Restart the nginx server
    sudo('service apache2 restart')


@hosts(['yutianxin.me'])
def shutdown():
    sudo('shutdown now')

