# `link_me`
This one was probably the simplest challenge.
The binary essentially told me what to do.
Tryng to run it, it complained that it couldn't find `libmumu.so`.
A quick `nm` hinted to me that `libmumu.so` should probably implement 2 functions: `array_sum` and `string_xor_with_key`.

Looking them up in `objdump` revealed their possible signatures:
```c
int array_sum(int *arr, size_t len);
void string_xor_with_key(char *str, size_t len, char key);
```

So I created `mumu.c` which implements the above functions and compiled it to a library using the `Makefile`.
You can get the flag running `make run`.
