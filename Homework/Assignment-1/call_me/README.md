# `call_me`
I initially tried a trick similar to the one I used for `call_main` and tried to change `__libc_start_main`'s first argument to the address of `call_me`.
Sadly, this time lightning didn't strike twice in the same place, so this approach didn't work.

My second thought was to somehow hack the function calls performed in `main`.
So I changed the file given to `open` as a parameter and then modified the third parameter of `read` so that it performs a buffer overflow to overwrite the saved `RIP` on the stack with the address of `call_me`.

![Sounds Good Doesn't Work](https://i.kym-cdn.com/entries/icons/original/000/024/153/soundsgood.jpg)

I haven't rolled back those changes to the `call_me` binary. If you run it, the buffer overflow still occurs and fails.
What I did was to replace `open`'s argument with `"payload"` and `read`'s third argument to 32.
24 would have been enough (8-byte "buffer" + saved `RBP` + saved `RIP`), but mistakes were made...

However, after the aforementioned failure, I noticed 5 `nop`s in `main`, right after the call to `close`.
Then it hit me: the opcode of the `call` mnemonic is 5 bytes long.
So the trick was to change those 5 `nop`'s to `call call_me`.
Since `call` refers its argument **relatively**, as an offset from the **next instruction**, I did some quick maths in order to produce the offset.
The maths went like this:
- the instruction after `call call_me` is `mov eax, 0`, which is stored at address `0x400710`.
- `call_me` is at address `0x400669`, so it's `0x400669 - 0x400710 = -0xa7` bytes away from our `call`.
- In 2's complement, `-0xa7` becomes `0xffffff59`, which is the offset we need.

Hence, the opcode: `e8 59 ff ff ff` (`e8` is the opcode for `call`).
