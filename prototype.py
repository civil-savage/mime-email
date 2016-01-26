#!/usr/local/bin/python

import smtplib
import argparse
from jinja2 import Environment, FileSystemLoader
from email.MIMEMultipart import MIMEMultipart
import os
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from PIL import Image
from base64 import b64encode

TEMPLATE_DIR="./"
J2 = Environment(loader=FileSystemLoader(TEMPLATE_DIR),
                     trim_blocks=True)
IMAGE_DIR="./images"

def main():
    images = os.listdir(IMAGE_DIR)
    encoded_images = {}
    strFrom = ''
    strTo   = ''
    msgRoot = MIMEMultipart('alternative')
    msgRoot['Subject'] = ""
    msgRoot['To'] = strTo
    msgRoot['From'] = strFrom
    msgRoot.preamble = 'This is a multi-part message in MIME format.'
    with open('text.txt', 'r') as text:
        text = text.read()
    msgRoot.attach(MIMEText(text))
    if not images:
        msgRoot.attach(MIMEText(render_template(), 'html'))
    else:
        msgRelated = MIMEMultipart('related')
        msgRelated.attach(MIMEText(render_template(images), 'html')) 
        for image in images: 
            with open(image, 'rb') as img: 
                byte_data = img.read()
                msgImage = MIMEImage(byte_data)
                msgImage.add_header('Content-ID', image)
                msgRelated.attach(msgImage)        
                b64 = b64encode(byte_data)
                encoded_images[image]=b64
        msgRoot.attach(msgRelated)
    with open("../../public_html/preview.html", 'w') as preview:
        preview.write(render_template(images, preview=encoded_images))
    print(msgRoot.as_string())
    # smtp = smtplib.SMTP('localhost')
    # smtp.sendmail(strFrom, strTo, msgRoot.as_string())
    # smtp.quit()

    
def render_template(images="", preview=None):
    img_data = {}
    for image in images: 
        img_data[str(image)] = list(Image.open(image).size)
        if preview:
            img_data[str(image)].append(preview[image])
    rt = J2.get_template('email.jinja').render( 
        img_data = img_data,
        preview = preview
    )
    return rt



if __name__ == "__main__":
    main()
