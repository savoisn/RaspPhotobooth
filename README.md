requierements :
```
sudo apt-get install build-essential python-dev
pip install uwsgi
```

setup dependencies : 
please use virtualenv
```
virtualenv venv # create the virtual env
source venv/bin/activate # activate it... 
pip install -r ./requierements.txt # install dependencies into the virtual env
```

stop the virtualenv with 
```
deactivate
```

debuging using the cli :
```
python PhotoBooth/PhotoBooth.py usename@emaildomain.com hello 50 0
```

running server for dev :
```
hug -f PhotoBooth/PhotoBooth.py
```

for production use : use uwsgi
```
uwsgi --http 0.0.0.0:8000 --wsgi-file PhotoBooth/Webserver.py --callable __hug_wsgi__
```

in order to send mail you need a smtp server listening on localhost
I used postfix and configured it with as a relay to my FAI smtp (smtp.free.fr)
Got into trouble with postfix not sending mail just after reboot... need to be restarted 
```
/etc/init.d/postfix restart
```

hope it helps

