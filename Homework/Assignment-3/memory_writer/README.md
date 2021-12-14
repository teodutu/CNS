# Memory writer
It seems every assignment has "one challenge to rule them all", so to speak.
For this assignment, I think this challenge is _the one_.

The program performs an arbitrary memory write itself.
It prompts the user for an address and a value and then writes that value at the specified address prints those 2 values, as well as the old value at the given address.
So we can also leak information.
The 2 numbers are read safely on 8 bytes using `scanf`.

An interesting caveat is that after perfroming the memory write and printing the information above, the program calls `exit(0)`, as opposed to returning.

## Stage 1: Run `main` in a loop
This actually turns into a benefit.
The first stage is to replace `exit@got` with the address of `main`.
The binary is stripped, so this address is taken from the first parameter of `__libc_start_main`, called by `_start`: `0x4011f8`.
This way, every call to `exit` actually re-runs `main`.

## Stage 2: Leak the address of `puts`
As I said above, the program also prints the old value at the given address.
So if we overwrite `puts@got`, we can get runtime the address of this function.
We can overwrite `puts@got` with what it contained **before the first call to `puts`**.
So we can replace it with the address of `puts@plt + 6`, where the resolver is beign called.
This way, we maitain the functionality of `puts` while also leaking its address in `libc`.

As always, we use this address to compute the address where `libc` is mapped and then the address of `system`.

## Stage 3: Call `system("/bin/sh")`... somewhat
We can easily overwrite `puts@got` with the address of `system`.
However, we also need to provide the string.

The binary also reads a name into a stack buffer.
Let's call it `"name"`.
This name is read safely with `fgets` with a proper buffer length.
No vulnerability here.

However, at the end of the function, the program calls `puts("Good luck, " + name)`.
The `"Good luck, "` part is slightly annoying, but we can ignore it by sending a name that looks like this `"|| /bin/sh"`.
This ends up calling system like so: `system("Good luck, || /bin/sh")`.
The first command (`"Good luck,"`) fails, which makes the second command to be run.
And this second command actually spawns a remote shell.
