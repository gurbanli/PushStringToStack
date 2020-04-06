# PushStringToStack
This tool helps for generating a part of shellcode which pushes given string to stack.

Basically, run install.sh as root. Tool will be installed as push2stack command.

Usage:
```
usage: push2stack.py [-h] [-s SOLUTION] STRING

positional arguments:
  STRING

optional arguments:
  -h, --help   show this help message and exit
  -s SOLUTION

Solutions for dealing with null bytes:

     1  -       Reproduce original value using add & sub
     2  -       XOR

```
Example:
```
root@kali:~# push2stack "You have been hacked by gurbanli"
\x68\x20\x20\x20\x00\x68\x61\x6e\x6c\x69\x68\x67\x75\x72\x62\x68\x20\x62\x79\x20\x68\x63\x6b\x65\x64\x68\x6e\x20\x68\x61\x68\x20\x62\x65\x65\x68\x68\x61\x76\x65\x68\x59\x6f\x75\x20

root@kali:~# push2stack "You have been hacked by gurbanli" -s 1
With null bytes: 45 bytes
Without null bytes: 52 bytes


\xbb\x0f\x0f\x0f\xef\x81\xc3\x11\x11\x11\x11\x53\x68\x61\x6e\x6c\x69\x68\x67\x75\x72\x62\x68\x20\x62\x79\x20\x68\x63\x6b\x65\x64\x68\x6e\x20\x68\x61\x68\x20\x62\x65\x65\x68\x68\x61\x76\x65\x68\x59\x6f\x75\x20
```
