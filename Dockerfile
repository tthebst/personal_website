FROM python:3.6
RUN pip3 install flask gunicorn
EXPOSE 80
COPY . /app
WORKDIR /app

CMD [ "gunicorn", "-w","2", "--threads" ,"4" ,"-b", "0.0.0.0:80","app:app" ]