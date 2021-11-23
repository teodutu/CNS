# Hello Service
The binary reads an input of at most `0x46` bytes, using `fgets`, and returns the following:
```
Hello, <input>
```

The output string is placed on the stack, at address `rbp - 0x50`
The input string is copied to it from the heap.
The amount of bytes copied is equal to `strlen(input)`.

At `rbp - 0x3c` lies the flag read (encrypted) by the `read_flag` function.
The encryption is weak, though.
It's simply: `flag[i] ^= i`

Anyway, the offset on the stack between the beginning of my input (after beign copied to the "Hello, " string) is `0x50 - 7 - 0x3c + 1 = 13`.
So by sending 13 bytes to the binary, we should leak the flag.

However, the problem here is that the binary places a `\0` character at the end of the output string (calculated using the same `strlen(input)` as before).

In order to fool this, we need, I'm appending a trailing `\0` character after 13 bytes of padding, so that the `\n` added by `sendline()` comes after this null byte.
This technique will leak 1 byte of the encrypted flag.
Another encrypted can be leaked by adding the same `\0` after 14 bytes of padding, and so on, until the whole encrypted flag is leaked.
