# PushStringToStack
This tool helps for generating opcodes which push given string to stack.

Basically, run install.sh as root. Tool will be installed as push2stack command.

Usage:
```
push2stack STRING
```
Example:
```
root@kali:~# push2stack "You have been hacked by gurbanli"
\x68\x00\x68\x61\x6e\x6c\x69\x68\x67\x75\x72\x62\x68\x20\x62\x79\x20\x68\x63\x6b\x65\x64\x68\x6e\x20\x68\x61\x68\x20\x62\x65\x65\x68\x68\x61\x76\x65\x68\x59\x6f\x75\x20
```
