FROM python:stretch

COPY . /main
WORKDIR main

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt


ENTRYPOINT ["python", "main.py"]