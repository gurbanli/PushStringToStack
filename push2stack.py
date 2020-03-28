#!/usr/bin/python3
import sys

def toHex(string):
    lst = []
    for ch in string:
        hexvalue = hex(ord(ch)).replace('0x', '\\x')
        lst.append(hexvalue)
    if ( (len(lst)+1) % 4 != 0 ):
        for i in range( 3-(len(lst) % 4)):
            lst.append('\\x20')
    lst.append('\\x00')
    return lst

string = ""
if ( len(sys.argv) != 2 ):
	print(f"Usage: {sys.argv[0]} STRING")
	sys.exit(1)
else:
    string = sys.argv[1]

ordered = toHex(string)

count = 0

newlist = []
for i in range(int(len(string)/4)+1):
    newlist.append(ordered[count:count+4])
    count = count + 4

shellcode = ""
for lst in newlist[::-1]:
    shellcode += "\\x68"
    for item in lst:
        shellcode += item

print(shellcode)
