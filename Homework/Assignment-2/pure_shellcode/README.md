# Pure Shellcode
The binary is very minimalistic.
Its main only performs 2 syscalls:
- `read(0, rbp - 0x40, 0x80)`
- `write(1, rbp - 0x40, 0x80)`

The buffer overflow is obvius, but the real vulnerability is the fact that `_start` pushes `rsp` onto the stack before calling `main`.
Because of this, the `write` syscalls leaks a stack address.
We can use this address to compute the address of the start of the local buffer in `main`.
Thus, the offset between these is `0x40 + 8 (call main) + 8 (push rbp) = 0x50`.

But in order to leak this address, we have to read some input, so we need a 2-stage attack where the shellcode comes in the second stage.


## Stage 1 - Leak the Address
The only thing we need in this stage is to overwrite the saved `rbp` with the address of `main` and read the leaked address from the binary's output.
This leak is then used to calculate the address of the beginning of the stack buffer.


## Stage 2 - Send the Shellcode
We overwrite the return address on `main`'s stack with the buffer address calculated above and inject the shellcode at the beginning of this buffer.
And this is it! 
