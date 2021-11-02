# `hidden`
I used GDB to perform this exploit.
But before that, I decompiled the binary usign Ghidra and saw that there are a few nameless functions.
Out of these, the most interesting one seemed to be the one at address `0x400599`.
Let's just call it `599`, for simplicity.
It was interesting because it performed some checks to its parameters and, if they were correct, it called `decrypt_flag` (which sounded promissing) and then printed what seemed to be the flag itself.

The parameters required by `599` are as follows:
- `rdi == 0x4e43`
- `rsi == 0x4353`
- `rdx == 0x4654`
- `rcx` is a string identical to `t_var` (so why not the same?)

To solve the challenge, I set the above registers in GDB and then changed `rip` to point to the start of `599`.
And that was it.
