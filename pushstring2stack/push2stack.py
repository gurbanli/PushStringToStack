#!/usr/bin/python3
from argparse import ArgumentParser, RawTextHelpFormatter
from avoid import solution_1, solution_2
from utils import generate_shellcode

solutions_string = """
Solutions for dealing with null bytes:\n\n\n
     1  -\tReproduce original value using add & sub
     2  -\tXOR
"""
parser = ArgumentParser(epilog=solutions_string,formatter_class=RawTextHelpFormatter)
parser.add_argument('string', metavar='STRING', type=str)
parser.add_argument('-s', action='store', metavar='SOLUTION', type=int)
args = parser.parse_args()

solution = args.s
text = args.string

if solution == 1:
    shellcode = generate_shellcode(text)
    without_null = solution_1(shellcode)
    print(f"With null bytes: {int(len(shellcode) / 4)} bytes")
    print(f"Without null bytes: {int(len(without_null) / 4)} bytes", end="\n\n")
    print(without_null)
elif solution == 2:
    shellcode = generate_shellcode(text)
    without_null = solution_2(shellcode)
    print(f"With null bytes: {int(len(shellcode) / 4)} bytes")
    print(f"Without null bytes: {int(len(without_null) / 4)} bytes", end="\n\n")
    print(without_null)
else:
    print(generate_shellcode(text))

