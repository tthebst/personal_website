FROM python:3.6
RUN pip3 install flask gunicorn boto3
EXPOSE 80
COPY . /app
ADD ./credentials.csv ~/.aws/
WORKDIR /app

#CMD [ "gunicorn", "-w","2", "--threads" ,"4" ,"-b", "0.0.0.0:80","app:app" ]
CMD exec gunicorn --bind 0.0.0.0:8080 --workers 1 --threads 8 app:app