FROM ubuntu:latest
MAINTAINER Joe Xu "joe.xu@daocloud.io"

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /RaspBerry
WORKDIR /RaspBerry

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["RaspBerry.py"]