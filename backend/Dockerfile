FROM python:3.7-alpine
COPY req.txt /
RUN pip install -r /req.txt
COPY main.py .
CMD [ "python", "./main.py" ]
EXPOSE 5000
