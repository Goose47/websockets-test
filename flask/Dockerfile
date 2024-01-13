FROM python:3.6
WORKDIR /app

#RUN apt-get install libssl-dev
#RUN CFLAGS="-I/usr/local/opt/openssl/include" LDFLAGS="-L/usr/local/opt/openssl/lib" UWSGI_PROFILE_OVERRIDE=ssl=true pip install uwsgi - no-binary :all:

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000
CMD [ "uwsgi", "--ini", "uwsgi.ini" ]
