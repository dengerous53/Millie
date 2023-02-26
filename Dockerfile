FROM python:3.10

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip install -U pip && pip install -U -r requirements.txt
WORKDIR /Millie-1

COPY start.sh /start.sh

CMD ["/bin/bash", "/start.sh"]
