import struct
from utils import to_four_digit_hex_format, generate_shellcode

"""
04.04.2020 Aydin Gurbanli

"""


OPCODES = {
    'MOV_EAX_': '\\xb8',
    'MOV_EBX_': '\\xbb',
    'ADD_EBX_': '\\x81\\xc3',
    'PUSH_EAX': '\\x50',
    'PUSH_EBX': '\\x53',
    'XOR_EAX_EBX': '\\x31\\xd8'


}


def solution_1(shellcode):
    first_num = shellcode[4:20]
    shellcode = shellcode[20:]
    from_value = to_four_digit_hex_format(first_num).replace('0x', '0x1')
    pushed_value = hex(int(from_value, 16)-int('0x11111111', 16))
    modified_shellcode = ''
    modified_shellcode += OPCODES['MOV_EBX_'] + ''.join('\\x{:02x}'.format(c) for c in struct.pack('<L', int(pushed_value,16)))
    modified_shellcode += OPCODES['ADD_EBX_'] + '\\x11\\x11\\x11\\x11' + OPCODES['PUSH_EBX']
    return modified_shellcode + shellcode


def solution_2(shellcode):
    first_num = shellcode[4:20]
    shellcode = shellcode[20:]
    hex_value = to_four_digit_hex_format(first_num)
    xor_value = int(hex_value, 16) ^ int('0x777777FF', 16)
    modified_shellcode = ''
    modified_shellcode += OPCODES['MOV_EAX_'] + '\\xff\\x77\\x77\\x77'
    modified_shellcode += OPCODES['MOV_EBX_'] + ''.join('\\x{:02x}'.format(c) for c in struct.pack('<L', xor_value))
    modified_shellcode += OPCODES['XOR_EAX_EBX']
    modified_shellcode += OPCODES['PUSH_EAX']
    return modified_shellcode + shellcode
