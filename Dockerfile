FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]