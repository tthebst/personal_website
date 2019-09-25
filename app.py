from flask import Flask
from flask import render_template
from flask import request, flash, redirect, url_for
import json
import os
import boto3
import io
from botocore.client import Config
app = Flask(__name__)


@app.route("/")
def hello():
    s = get_txt_aws("hallo.txt")
    print(s)

    return render_template("home.html", s=s)


def get_txt_aws(filename):
    s3 = boto3.client('s3',
                      # aws_access_key_id=os.environ['AWS-ACCESS-KEY-ID'],
                      # aws_secret_access_key=['AWS-SECRET-ACCESS-KEY'],

                      config=Config(signature_version='s3v4'),
                      region_name='eu-central-1'
                      )
    bytes_buffer = io.BytesIO()
    obj = s3.download_fileobj(Bucket="my-personal-website-tim", Key=filename, Fileobj=bytes_buffer)

    byte_value = bytes_buffer.getvalue()
    print(byte_value)
    str_value = byte_value.decode()
    print(str_value)
    return str_value
