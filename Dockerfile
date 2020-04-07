FROM python:3.7.6

COPY . /main
WORKDIR main

RUN pip3 install --upgrade pip3
RUN pip3 install -r requirements.txt


ENTRYPOINT ["python3", "main.py"]