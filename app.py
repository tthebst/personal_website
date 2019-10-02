from flask import Flask
from flask import render_template
from flask import request, flash, redirect, url_for
import json
import os
import boto3
import io
import random
from botocore.client import Config
app = Flask(__name__)


@app.route("/")
def hello():
    aboutme = get_txt_aws("aboutme.txt")
    resume = get_signed_url("resume.pdf")

    return render_template("home.html", aboutme=aboutme, resume=resume)


@app.route("/wallpapers")
def wallpapers():
    picture_list = get_s3_client().list_objects(Bucket="my-personal-website-tim", Prefix="wallpapers/")
    picture_urls_all = []
    random_pictures_i = random.sample(range(1, len(picture_list['Contents'])), 10)
    picture_urls_random = []
    print("======")
    for i in range(0, len(picture_list['Contents'])):
        picture_urls_all.append(get_signed_url(picture_list['Contents'][i]['Key']))
        if i in random_pictures_i:
            picture_urls_random.append(get_signed_url(picture_list['Contents'][i]['Key']))

    return render_template("wallpapers.html", picture_urls_all=picture_urls_all[1:], picture_urls_random=picture_urls_random, showall=False)


@app.route("/wallpapers_all")
def wallpapers_all():
    picture_list = get_s3_client().list_objects(Bucket="my-personal-website-tim", Prefix="wallpapers/")
    picture_urls_all = []
    random_pictures_i = random.sample(range(1, len(picture_list['Contents'])), 10)
    picture_urls_random = []
    print("======")
    for i in range(0, len(picture_list['Contents'])):
        picture_urls_all.append(get_signed_url(picture_list['Contents'][i]['Key']))
        if i in random_pictures_i:
            picture_urls_random.append(get_signed_url(picture_list['Contents'][i]['Key']))

    return render_template("wallpapers.html", picture_urls_all=picture_urls_all[1:], picture_urls_random=picture_urls_random, showall=True)


def get_txt_aws(filename):
    s3 = get_s3_client()
    bytes_buffer = io.BytesIO()
    obj = s3.download_fileobj(Bucket="my-personal-website-tim", Key=filename, Fileobj=bytes_buffer)
    byte_value = bytes_buffer.getvalue()
    print(byte_value)
    str_value = byte_value.decode()
    print(str_value)
    return str_value


def get_s3_client():
    s3 = boto3.client('s3',
                      # aws_access_key_id=os.environ['AWS-ACCESS-KEY-ID'],
                      # aws_secret_access_key=['AWS-SECRET-ACCESS-KEY'],

                      config=Config(signature_version='s3v4'),
                      region_name='eu-central-1'
                      )
    return s3


def get_signed_url(location):
    s3 = get_s3_client()
    url = s3.generate_presigned_url(
        ClientMethod="get_object", Params={"Bucket": "my-personal-website-tim", "Key": location}
    )
    print(url)
    return url
