FROM ubuntu:latest

MAINTAINER Sezer Bozkir "admin@sezerbozkir.com"
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
RUN apt-get install -y net-tools
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
# CMD ["python3", "dummy_processes.py"]
ENTRYPOINT ["python3"]
CMD ["setup.py"]



# COPY ./requirements.txt /requirements.txt
# RUN pip install -r requirements.txt


# WORKDIR /app
# RUN python setup.py
