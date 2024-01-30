FROM python:3.6
WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000
CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
