## Docker

### Start new project. Creates app folder with manage.py etc...
`docker-compose run --rm app sh -c "django-admin startproject app"`

`docker-compose run --rm app sh -c "python manage.py startapp bitmex"`

`docker-compose run --rm app sh -c "python manage.py makemigrations"`

`docker-compose run --rm app sh -c "python manage.py createsuperuser"`

`docker-compose run --rm app sh -c "python manage.py test leads"`

`sudo docker-compose run --user=root --rm proxy sh -c "chown -R nginx:nginx /etc/letsencrypt"`

`sudo docker-compose run --user=root --rm proxy sh -c "ls -la/etc/letsencrypt"`

`sudo docker rmi $(sudo docker images --filter "dangling=true" -q --no-trunc)`

`sudo docker volume rm $(sudo docker volumes ls --filter "dangling=true" -q --no-trunc)`

`sudo docker volume rm $(sudo docker volume ls -q)`

### django-mailer https://github.com/pinax/django-mailer/
`* * * * * (docker-compose -f /home/admin/lead_market/docker-compose-nextjs.yml exec --user=root -T app /py/bin/python /app/manage.py send_mail >> /cron_mail.log 2>&1)`


