# `call_me_reloaded`
I changed the 5 `nop`s at the end of `main` with a `call` instruction similar to what I did for the `call_me` binary.
However, this was not enough.
By inspecting the code decompiled by Ghidra, I saw that now `call_me` now requires 2 parameters:
- `rdi == 0x1337`;
- `rsi` is a string whose first 3 characters are `CNS`.

There are 2 instructions above the `call call_me` that I inserted, which tamper with those specific registers.
So I changed those `mov`s to store the correct data in `rdi` and `rsi`.
I found the address of `CNS` by using `xxd` on the binary.
It's at offset `0x691` in the `.text` section.
Since the `.text` section is mapped at address `0x400000`, the address of `"CNS"` is `0x400691`.
