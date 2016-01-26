# mime-email

More or less a fork of a project I started earlier and now want to develop further of a script that creates HTML emails.  Currently, adjusting the script to be more general purpose (see prototype for original specifications).  I am trying to strip this down to being a pure command line too as opposed to being tied to specific filenames/locations and then trying to implement the functionality of the original script or perhaps write additional scripts. 

Purpose
-------
This script t will take a plain text file, and HTML file, and any number of images and create a valid MIME email that can be sent.  


Development
-----------
Possible avenues for future development.

 * Write to a file instead of relying on a pipe/copy from command prompt
 * Correct any formatting issues 
 * Add autosend functionaily (smtp specify to/from etc, see prototype)
 * Add possible preview mode (as suggested in the prototype).


