FROM python:3.9

WORKDIR /app

# install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/

# port for Flask app
EXPOSE 5000

# start the app
CMD exec gunicorn --bind :5000 app:app --workers 1 --threads 1
