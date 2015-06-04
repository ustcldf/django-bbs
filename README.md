This is a BBS powered by Django1.8
2015.06.03
Deploy:
If you have a totally new installed Ubuntu system(I used Ubuntu14.04 as server), You may do as follows to deploy this web application.

1.Copy sourcecode to "/home/xxx" or other dir convenient

2.Update your system:
sudo apt-get update
you may need to install "unzip" or something that a new system may not contains

3.Check if gcc, g++ installed or not,if not:
sudo apt-get install gcc g++

4.You need mysql as database:
sudo apt-get install mysql-server

#I set mysql root password z as example here(consistent with settings.py file)

mysql -uroot -pz
 >>create database feedback default charset utf8;

sudo apt-get install libmysqld-dev

5.Install python-dev:
sudo apt-get install python-dev

6.Install python-setuptools:
python setup.py install

7.Install pip:
easy_install pip

8.Install django-tastypie(must be this version)
https://github.com/django-tastypie/django-tastypie.git

9.Install python packages:
pip install -r requirements.txt

10.run it!(First ensure settings.py configured correctly)
python manage.py runserver 0.0.0.0:8000


Enjoy! #^__^#
