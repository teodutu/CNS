# Strict Shellcode
By far the coolest task.
It's kind of a classic: the binary reads an input string, which is `memcpy`'d to a page that was previously `mmap`-ped with read, write and execute permissions and then calls executes this page as a function.
However, there's one catch: the shellcode is **sanitised** and can't contain any of the following bytes:
- `0x0`
- `0x3b`
- `0x62`
- `0x69`
- `0xf`
- `0x5`

The chosen solution is typical: the shellcode is made up of two parts:
- the second part is an `execve("/bin/sh")` shellcode, but all its bytes have been xor-ed with `0x2` (chosen via trial and error)
- the first part decrypts the second one
