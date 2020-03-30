#!/usr/bin/python3
import sys, argparse

def toHex4Shellcode(string):
    lst = []
    for ch in string:
        hexvalue = hex(ord(ch)).replace('0x', '\\x')
        lst.append(hexvalue)
    if ( (len(lst)+1) % 4 != 0 ):
        for i in range( 3-(len(lst) % 4)):
            lst.append('\\x20')
    lst.append('\\x00')
    return lst

def toHex4Disassembly(string):
    lst = []
    for ch in string:
        hexvalue = hex(ord(ch)).replace('0x', '')
        lst.append(hexvalue)
    if ( (len(lst)+1) % 4 != 0 ):
        for i in range( 3-(len(lst) % 4)):
            lst.append('20')
    lst.append('00')
    return lst

def disassemble(ordered,string):
    count = 0
    newlist = []
    for i in range(int(len(string)/4)+1):
        newlist.append(ordered[count:count+4])
        count = count + 4
    disassembler_output = ""
    for lst in newlist[::-1]:
        disassembler_output += f'PUSH 0x{"".join(str(item) for item in lst[::-1])}\n'
    return disassembler_output
def generateShellcode(ordered, string):
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
    return shellcode

parser = argparse.ArgumentParser()
parser.add_argument('string', metavar="STRING", type=str)
parser.add_argument('-d', '--disassemble', action='store_true', help='disassemble push instructions with values')
args = parser.parse_args()

string = args.string
if args.disassemble:
    print(disassemble(toHex4Disassembly(string),string))
else:
    print(generateShellcode(toHex4Shellcode(string),string))
