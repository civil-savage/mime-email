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



IMAGE_DIR="./images"

def main():
    images = os.listdir(IMAGE_DIR)
    encoded_images = {}
    msgRoot = MIMEMultipart('alternative')
    msgRoot.preamble = 'This is a multi-part message in MIME format.'
    with open('text.txt', 'r') as src_text:
        text = text.read()
    with open('email.html','r') as src_html:
        html = src_html.read()
    msgRoot.attach(MIMEText(text))
    if not images:
        msgRoot.attach(MIMEText(html, 'html'))
    else:
        msgRelated = MIMEMultipart('related')
        msgRelated.attach(MIMEText(html, 'html')) 
        for image in images: 
            with open(image, 'rb') as img: 
                byte_data = img.read() # This needs to get sorted out
                msgImage = MIMEImage(byte_data)
                msgImage.add_header('Content-ID', image)
                msgRelated.attach(msgImage)        
                b64 = b64encode(byte_data)
                encoded_images[image]=b64
        msgRoot.attach(msgRelated)
    print(msgRoot.as_string())

    



if __name__ == "__main__":
    main()
