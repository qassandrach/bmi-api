FROM python:3.8-alpine

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

WORKDIR /usr/src

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app /usr/src/app

WORKDIR /usr/src/app

EXPOSE 5000

CMD ["python", "app.py"]