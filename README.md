# Ziprisk.us

Simple Flask using SQLAlchemy and SQLite database.
queries and displays census data by zip code

For styling [semantic-ui](https://semantic-ui.com/) is used.

### Setup
configuring the server 

```console
sudo apt update
sudo apt upgrade
sudo apt install git
sudo apt install apache2
```

clone the project 

```console
cd /var/www
git clone https://github.com/jlmartin3/ziprisk.us
cd /ziprisk.us
```

create the virtual envrioment 

```console
sudo apt install pipenv
pipenv install
pipenv --venv
```

Activate it and install packages

```console
. venv/bin/activate
pip install Flask
pip install Flask-SQLAlchemy
export FLASK_APP=app.py
export FLASK_ENV=development
deactivate
```

Set ownership of directoy to user www-data
required by apache2 to host app

```console
ls -ld /var/www/ziprisk.us
sudo addgroup site1
sudo adduser www-data site1
groups www-data
sudo chown -vR :site1 /var/www/ziprisk.us/
sudo chmod -vR g+w /var/www/siprisk.us/
ls -ld /var/www/ziprisk.us
```


edit configuration file

```console

sudo nano /etc/apache2/sites-available/ziprisk.us.conf

```

paste the following

```console

<VirtualHost *:80>
    ServerName ziprisk.us
    ServerAlias www.ziprisk.us
    ServerAdmin contactjamesmartin@gmail.com

    WSGIDaemonProcess flaskapp user=www-data group=www-data threads=5
    WSGIScriptAlias / /var/www/ziprisk.us/app.wsgi


    <Directory /var/www/ziprisk.us>
        WSGIProcessGroup flaskapp
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
        Require all granted
    </Directory>

    Alias /static /var/www/ziprisk.us/static

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>


```


deploy with apache2

```console

sudo apt-get install libapache2-mod-wsgi-py3
sudo a2enmod wsgi

sudo apachectl configtest
sudo apachectl restart

```



























