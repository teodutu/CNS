# Call Me
This one was weird.
I don't claim to have done it properly, but I did it nonetheless.

As in the previous assignment, I think the trick was to use the space provided by the `nop` at the end of `main` to `call __call_me`.
`__call_me` is "hidden" (in plain sight) in the .data section of the binary.
Anyway, I palced a `call __call_me` instruction preceded by 2 `nop`s before `leave ; ret` and... nothing.

I guess I wasn't running the program with the right parameter.
So I ran it in gdb and followed the execution of `__call_me`.
I noticed it contains a loop between addresses `0x401614` and `0x401643`, in which the flag is calculated and placed on the stack.
So I just took it from there.

Remember: if it's stupid and it works, it ain't stupid.
