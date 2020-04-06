"""
04.04.2020 Aydin Gurbanli

"""


def to_backslash_format(text):
    newlist = []
    for ch in text:
        hex_value = hex(ord(ch)).replace('0x', '\\x')
        newlist.append(hex_value)
    if len(newlist) + 1 % 4 != 0:
        for i in range(3 - (len(newlist) % 4)):
            newlist.append('\\x20')
    newlist.append('\\x00')
    return newlist


def to_four_digit_hex_format(shellcode):
    shellcode_list = list(shellcode.replace('\\x', ''))
    x = len(shellcode_list)
    hex_string = '0x'
    for i in range(x, 0, -2):
        for char in shellcode_list[i - 2:i]:
            hex_string += char
    return hex_string


def generate_shellcode(text):
    count = 0
    newlist = []
    hex_chars = to_backslash_format(text)
    for i in range(int(len(text) / 4) + 1):
        newlist.append(list(hex_chars)[count:count + 4])
        count = count + 4
    shellcode = ""
    for lst in newlist[::-1]:
        shellcode += "\\x68"
        for item in lst:
            shellcode += item
    return shellcode

