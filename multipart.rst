multipart
#########

Name 
----- 
     multipart - build valid HTML email taking a plain text and
     HTML file, can take an arbitrary number of images to embed in base64

SYNOPSIS
--------
::
   **multipart ** HTML_FILE TEXT_FILE -i image_file_ paths 

DESCRIPTION
-----------

     multipart is designed to take a HTML file, a text file, and an
     optional number of images files and create a multipart HTML email
     that is create with the valid MIME types for the various parts of
     the email.  The HTML file and the text file are required while
     the images are completely optional.


OPTIONS
-------



    **-i --images images** 
        Image files to be attached to the email.  These will be base64
        encoded and attached as text to the email. 
    

OUTPUT
------

     The output of this file is a string sent to standard
     out. Currently there is no option to specifiy a file to write to
     but it is currenly being developed. 

    

