#!/usr/bin/python3

#    pynstr
#    Copyright (C) 2015  Matthias Krüger

#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 1, or (at your option)
#    any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston MA  02110-1301 USA


from subprocess import check_output
import sys
from collections import Counter
__author__ = 'Matthias "matthiaskrgr" Krüger'


BINARY = sys.argv[1]
print(BINARY)
print("Reading binary and counting instructions...\n")
command = [ "llvm-objdump",  "-disassemble", "-no-show-raw-insn", "-no-leading-addr", "-no-discriminators", str(BINARY)]
output = check_output(command)
output = str(output).replace('\\n', '\n').replace('\\t', '\t') # format


instrs = [] # list of all instrs
for line in output.splitlines():
	splitline = line.split()
	if (len(splitline) >= 2):
		instr = splitline[1]
		instrs.append(instr)


for i in Counter(instrs).most_common(): # count instrs
	print(str(i[1]) + " " + str(i[0]))

print()
print(str(len(instrs)) + " instructions")
print(str(len(Counter(instrs).most_common())) + " unique instructions")
