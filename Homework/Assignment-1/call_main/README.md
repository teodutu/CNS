# `call_main`
The issue with this binary was that at compile-time, its "main" (i.e. the function called by `__libc_start_main`) had been set to `dummy`.
More precisely, the first parameter of `__libc_start_main` was `0x400549`, instead of `0x40055a`, which is the address of `main`.
Thus, I modified the `mov` instruction at address `0x40041d` so that `rdi` (the first argument of `__libc_start_main`) now stores the correct address of `main`: `0x40055a`.
