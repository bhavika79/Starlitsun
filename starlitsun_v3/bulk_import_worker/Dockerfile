FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install mysql-connector-python

CMD ["python","import_products.py"]