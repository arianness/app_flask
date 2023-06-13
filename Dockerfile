FROM python:3.8.16-alpine
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
ENV PORT=5000
RUN pip install -r requirements.txt
COPY . /opt/app

CMD ["flask","run"]
EXPOSE 5000