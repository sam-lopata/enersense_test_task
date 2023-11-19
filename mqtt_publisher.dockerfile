FROM python:3.9.1
RUN mkdir /app
WORKDIR /app
COPY mqtt/requirements.txt /app/requirements.txt
COPY mqtt/pub.py ./
RUN pip install -r requirements.txt

CMD [ "python", "-u", "./pub.py"]