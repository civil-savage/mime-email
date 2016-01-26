#!/usr/local/bin/python

import argparse
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

parser = argparse.ArgumentParser(description='Builds an multi-part html email')
parser.add_argument('html_file', action="store", help='A HMTL file that will become the HTML portion the email')
parser.add_argument('text_file', action="store", help='A text file that will become the text portion of the email')
parser.add_argument('-i', action="append", help='adds images to the email')
args = parser.parse_args()

HTML_FILE = args.html_file
TEXT_FILE = args.text_file
IMAGES    = args.i

def main():
    msgRoot = MIMEMultipart('alternative')
    msgRoot.preamble = 'This is a multi-part message in MIME format.'
    with open(TEXT_FILE, 'r') as txt_f:
        text = txt_f.read()
    with open(HTML_FILE,'r') as html_f:
        html = html_f.read()
    msgRoot.attach(MIMEText(text))
    if not IMAGES:
        msgRoot.attach(MIMEText(html, 'html'))
    else:
        msgRelated = MIMEMultipart('related')
        msgRelated.attach(MIMEText(html, 'html')) 
        for image in IMAGES: 
            with open(image, 'rb') as img: 
                msgImage = MIMEImage(img.read())
                msgImage.add_header('Content-ID', os.path.split(image)[1]) ## clean up to remove the folder location in the for cid
                msgRelated.attach(msgImage)        
        msgRoot.attach(msgRelated)
    print(msgRoot.as_string()) 


if __name__ == "__main__":
    main()
