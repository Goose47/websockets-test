FROM python:3.6
WORKDIR /app
RUN apt-get update
RUN apt-get install -y \
     build-essential \
     libssl-dev python3-dev \
     python3-venv

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ['uwsgi', '--http', ':5000', '--gevent', '1000', '--http-websockets', '--master', '--wsgi-file', 'main.py', '--callable', 'app']

# CMD [ "uwsgi", "--ini", "uwsgi.ini" ]
