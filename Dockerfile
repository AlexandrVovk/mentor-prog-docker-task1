FROM python:3.10-alpine

WORKDIR /app
COPY app.py ./
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]