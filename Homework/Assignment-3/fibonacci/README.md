# Fibonacci
These challenges are starting to look very similar to each other at this point...

The binary reads an index `n` and outputs the `n`-th fibonacci number.
This is performed in a `while (1)` loop.
The index is as a string into a buffer, using `gets` (red flag: buffer overflow here!)
This index is somewhat sanitised, i.e. it can only be within the `[-46, 46]` interval. 
Otherwise, the infinite loop breaks.

So we perform a classic attack: we leak the address of `puts`, calculate the address where `libc` is mapped, then, using a second payload, we overwrite the return address to call `system("/bin/sh")`, using ROPs.
