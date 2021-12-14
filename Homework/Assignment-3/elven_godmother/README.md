# Elven godmother
The binary reads 2 names and a gender (the binary is a bigot for only allowing males and females!!111!!!).
Each name can be at most 256 characters long.
They are read by `fgets` into proprely sized stack buffers.
No vulnerability here.

However, the 2 names are concatenated by the `mix_names` function with `strcat` into a stack buffer of only `268` bytes.
That's where the overflow happens.
This allows us to leak the address of `puts` from `libc`, by calling `puts@plt(puts@got)`.
As always, we use this address to calculate the address from which `libc` is mapped and then to obtain the addresess of `system` and `"/bin/sh"`.

The second payload overwrites the return address with that of `system`, whose argument is that of `"/bin/sh"`.
