FROM python:3.9.5

RUN mkdir /web_app

COPY requirements.txt /web_app/

COPY main.py /web_app/

RUN python -m pip install -r /web_app/requirements.txt

WORKDIR /web_app

ENTRYPOINT ["python", "main.py"]





