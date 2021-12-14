# Canary
The binary asks for either `'y'` or `'n'`.
When sending a payload that contains `'n'`, the `run` function returns.
When sending a payload that contains `'y'`, the reading loop continues and the input is printed likes so `printf(input)`.
This `printf` is vulnerable as it can leak information.
The binary reads input into a 24-byte buffer, which is followed by a canary.
Moreover, the input is read using `gets`, so we have a free hand to do overflows.

As a result, the first stage of the exploit aims to leak the canary.
We can do this by sending a payload containing `'y'` and `%9$lx`.
The last part is the 10th argument of `printf`.
On a 64-bit system, the first 6 arguments are registers.
Starting from the 7th, the parameters are passed on the stack.
Hence, the 10th 8-byte argument (`%lx`) is 24 bytes above `printf`'s stack frame, i.e. precisely where the canary is placed.

For the second stage, we use the leaked canary to overwrite the return address with that of `flaggy`, which calls `system("cat /home/ctf/flag")`.
