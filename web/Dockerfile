FROM python:3.8

WORKDIR /code

COPY requirements.txt /code

RUN pip install --upgrade pip
RUN pip install -r requirements.txt 
    # && rm -rf /root/.cache

COPY . .

EXPOSE 5000
CMD ["python3", "index.py"]
# CMD gunicorn --bind 0.0.0.0:5000 --workers=3 --threads=3 index:server