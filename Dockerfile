from ubuntu:14.04
MAINTAINER Oscar <zhaoshuailong09@163.com>
MAINTAINER Nolan Zhao <2928807616@qq.com>

ENV DJANGO_BBS_VERSION 0.1.0

COPY ./bbs_20150603 /usr/src/app

RUN apt-get update -y && \
	apt-get install python-dev libmysqld-dev && \
	wget https://bootstrap.pypa.io/ez_setup.py -O - | python && \
	easy_install pip && \
	git clone https://github.com/django-tastypie/django-tastypie.git && \
	cd django-tastypie && \
	python setup.py install && \
	cd .. && \
	rm -rf django-tastypie && \
	pip install

ADD run.sh /run.sh
RUN chmod +x /*.sh

# Expose environment variables
ENV DB_HOST **LinkMe**
ENV DB_PORT **LinkMe**
ENV DB_NAME feedback
ENV DB_USER admin
ENV DB_PASS **ChangeMe**

EXPOSE 80
CMD ["/run.sh"]
