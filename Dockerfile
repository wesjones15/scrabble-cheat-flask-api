FROM python:3

ADD views.py /

RUN pip install flask
RUN pip install flask-cors

CMD [ "python", "views.py" ]