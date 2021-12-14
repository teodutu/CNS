# Canary 2
For this challenge, the `run` function is identical to that of [`canary`](../canary).
The ony difference is that this time there is no `flaggy` function.

The solution is to replace the second stage from calling `flaggy` to using a gadget to call `puts@plt(puts@got)` in order to leak the runtime address of `puts`, from which we can compute the address from which `libc` is mapped and then the addresses of `system` and `"/bin/sh"`.
The latter 2 addreses are used for a third stage payload in by which we get a remote shell.
At the end, in order to trigger both the second and third payloads, we send an `'n'` to the binary in order to trigger those payloads.
