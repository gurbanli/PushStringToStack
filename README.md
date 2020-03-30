# PushStringToStack
This tool helps for generating opcodes which push given string to stack.

Basically, run install.sh as root. Tool will be installed as push2stack command.

Usage:
```
usage: push2stack.py [-h] [-d] STRING

positional arguments:
  STRING

optional arguments:
  -h, --help         show this help message and exit
  -d, --disassemble  disassemble push instructions with values

```
Example:
```
root@kali:~# push2stack "You have been hacked by gurbanli"
\x68\x20\x20\x20\x00\x68\x61\x6e\x6c\x69\x68\x67\x75\x72\x62\x68\x20\x62\x79\x20\x68\x63\x6b\x65\x64\x68\x6e\x20\x68\x61\x68\x20\x62\x65\x65\x68\x68\x61\x76\x65\x68\x59\x6f\x75\x20

root@kali:~# push2stack "You have been hacked by gurbanli" -d
PUSH 0x00202020
PUSH 0x696c6e61
PUSH 0x62727567
PUSH 0x20796220
PUSH 0x64656b63
PUSH 0x6168206e
PUSH 0x65656220
PUSH 0x65766168
PUSH 0x20756f59
```
