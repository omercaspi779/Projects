#!/usr/bin/env python3
from pwn import *
import os
import socket


# start of args 
args = ["A"]*100
args[0] = './input2'
args[65] = '\x00'
args[66] = '\x20\x0a\x0d'
args[67] = '4444'
# end of args - total 100 args as asked 


# env variables input
env = {
	  # name of the env    # value of it
    b'\xde\xad\xbe\xef': b'\xca\xfe\xba\xbe'
}


r1, w1 = os.pipe()
r2, w2 = os.pipe()
os.write(w1, b'\x00\x0a\x00\xff') # stdin
os.write(w2, b'\x00\x0a\x02\xff') # stderr

#file input:
           #name
with open('\x0a', 'w') as f:
    f.write('\x00\x00\x00\x00')


s = ssh(host="pwnable.kr", port=2222, user="input2", password="guest")
io = s.process(
    executable='./input2',
    argv=args,
    env=env,
    stdin=r1,
    stderr=r2
)

# io.recvuntil(b'Just give me correct inputs then you will get the flag :)\n')
print(io.recvline().decode())
print(io.recvline().decode())
print(io.recvline().decode())
print(io.recvline().decode())

#socket input:

conn = remote('localhost', 4444)
conn.sendline(b'\xde\xad\xbe\xef')


print(io.recvline().decode())




io.interactive()


