FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip3 install -r requirements.txt
ENV FLASK_APP=bmi.py 
ENV FLASK_ENV=development

COPY bmi.py .

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]