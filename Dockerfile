FROM python:3.9

WORKDIR /app

# install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/

# port for Flask app
EXPOSE 5000

# start the app
CMD ["python", "app.py"]