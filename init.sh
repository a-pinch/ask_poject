#! /bin/bush

if [[ ! -e ~/web ]]
then
	mkdir ~/web
	echo "~/web created"
fi
cd ~/web
echo "cd ~/web"

if [[ ! -e log ]]
then
	mkdir log
	echo "log dir created"
fi

if [[ ! -e etc ]]
then
	mkdir etc
	echo "etc created"
fi
if [[ ! -e uploads ]]
then
	mkdir uploads
	echo "uploads created"
fi
if [[ ! -e public ]]
then
	mkdir public
	echo "public created"
fi

cd public
echo "cd public"

if [[ ! -e img ]]
then
	mkdir img
	echo "create img"
fi
if [[ ! -e css ]]
then
	mkdir css
	echo "create css"
fi
if [[ ! -e js ]]
then
	mkdir js
	echo "create js"
fi

if [[ ! -h /etc/nginx/sites-enabled/test.conf ]]
then
	echo "create link to test.conf"
	sudo ln -s ~/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
fi
sudo rm /etc/nginx/sites-enabled/default

echo "starting nginx ..."
sudo /etc/init.d/nginx restart

echo "startin gunicorn ..."
cd ~/web
gunicorn -c /home/box/web/etc/hello.py hello:application --daemon -p /home/box/web/log/hello.pid
gunicorn -c /home/box/web/etc/django.py wsgi --daemon -p /home/box/web/log/gjango.pid
