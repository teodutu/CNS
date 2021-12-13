# Uninitialized
The program reads a number `n` as a string of at most 6 bytes.
It then reads another string at `buf + n + 16`.

The program prints the flag if `buf` is `"Where is the flag?"`.
This is not possible, as the second `fgets` only reads 16 bytes and `strlen("Where is the flag?") = 18`.

So we need to hack the function that performs the check.
Luckily, it uses the uninitialised (wink, wink) variable `n` to calculate `strlen(buf + n)`.
More specifically, if we overwrite `n` to be `strlen(buf)`, then `strlen(buf + n)` will be 0.
In this case, the `strncmp` that uses this result will have nothing to compare and, thus, return 0.

The combination of the 2 `fgets` calls equates to an arbitrary memory write.
Using `gdb`, I computed the offset between `n` and `buf` and found that it's `-2148`.
As I said above, at this offset, we need to write the length of "Where is the flag?".
That's all.
