#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

cp push2stack.py /usr/bin/push2stack
chmod +x /usr/bin/push2stack

echo "Now you can use this tool as push2stack command !"
