FROM python:3.6
WORKDIR /app

RUN apt-get install \
     build-essential \
     libssl-dev python3-dev \
     python3-venv

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000
CMD [ "uwsgi", "--ini", "uwsgi.ini" ]
