FROM ubuntu:20.04


RUN apt update -y; apt install -y \
        python3 \
        python3-pip


COPY app.py app.py
COPY requirements.txt requirements.txt

# INSTALL REQUIREMENTS
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# COPY FILES
WORKDIR OperSo
COPY static static
COPY upload upload
COPY templates templates
COPY src src
COPY app.py app.py

EXPOSE 8080

ENTRYPOINT python3 app.py
