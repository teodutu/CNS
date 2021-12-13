# Piece of PIE
This one is easy: the program contains the function `make_it_easy`, which performs `system("/bin/sh")`.
There's a buffer overflow in `main`, by which we can overwrite the function's return address with that of `make_it_easy`.

However, due to issues with stack alignment, the exploit fails if using the function's address directly.
As a result, we need to skip its prologue in order to keep the stack aligned to 16 bytes.
