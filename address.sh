#!  /usr/bin/bash

echo "ala ma kota"

ip address | grep "dynamic" | awk '{print $2}' | cut -d'/' -f1
