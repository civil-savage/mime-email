#!/bin/bash

echo "Editing input textfile..."

python3 ~/tmail/tmp_email_edit.py ${3}

bodyfile=email_replacement_file.txt

echo "Edit complete, ...preparing message"

timestamp ${bodyfile}


thunderbird -compose to="${1}" ,subject="${2}" ,body="$(cat ${bodyfile})"

echo "Message composed and is awating confimation."

echo "Clean up temporary file?"
select yn in "Yes" "No"; do
    case $yn in
	Yes ) rm email_replacement_file.txt; echo "Clean up complete"; break;;
	No ) exit;;
    esac
done


