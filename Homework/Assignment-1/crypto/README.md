# crypto
By far the shortest task.
After decompiling the binary using Ghidra, renaming and retyping some parameters in `enc_init`, I figured out that it generates a permutation, based on the key.
And then it's this permutation that's actually used for encryption.
The only encryption algorithm that I know of and that does this kind of trick is **RC4**.
And RC4 it was.
I assumed that the flag would be the symbol `bonus_flag`, so I inspected the memory there using GDB and took **everything** under this symbol.
Then I placed this data inside the `decrypt_rc4.py` script, which uses Python's `ARC4` library.

And everything worked smoothly.
Sometimes, ignorance really is bliss...

By the way, the flag's format is wrong.
It should be `CNS_CTF{Stream_ciphers_for_the_win}`, not `CNSCTF_{Stream_ciphers_for_the_win}`.
