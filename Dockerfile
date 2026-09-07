FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install pandas numpy

CMD ["python", "Bright.py"]