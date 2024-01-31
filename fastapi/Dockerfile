FROM python:3.6
WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
#CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
