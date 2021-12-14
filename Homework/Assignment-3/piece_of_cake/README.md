# Piece of cake
It truly is so.

The program reads a string of at most 80 bytes into a 32-byte buffer.
So here's the vulnerability.
There is also a function that calls `system("ls")`.

The attack is a basic ROP chain that calls the address of `call system` (`0x40117f`) using a `pop rdi ; ret` gadget in order to change `system`'s argument from `"ls"` to `"sh"`.
The string `"sh"` already exists in the binary file.
How convenient?
