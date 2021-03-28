FROM python:3.7

WORKDIR /monitoring_script

COPY requirements.txt .

COPY test_files ./test_files

ADD . ./monitoring_script

ENV SECRET=clmjSMUpmLkFoTDmAUERocsvnmNS+r25xcfOjP3g
ENV ACCESS_KEY=AKIAQSPNLRJYQFHUJLGS
ENV BUCKET_NAME=tech-interview-2513


# Install the dependencies
RUN pip install -r requirements.txt

CMD ["python","./monitoring_script/main.py"]