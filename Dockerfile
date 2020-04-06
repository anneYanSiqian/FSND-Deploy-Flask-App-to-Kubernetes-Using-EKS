FROM python:3.7.2

COPY . /main
WORKDIR main

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt


ENTRYPOINT ["python3", "main.py"]