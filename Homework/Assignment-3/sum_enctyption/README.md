# Sum encryption
The program uses `scanf` to first read a number of numbers.
Let's call this number `num`.
This number is ignored as the program then proceeds to read however many 8-byte values into a 17-element stack array, until `EOF`.
Then the first `num` elements of the array are added together and the result is xored with a random 64-bit value.
The result of this operation is printed to `stdout`.

The random number is generated using `srand(time(0))` followed by 2 calls to `rand()` like so: `(long)rand() | (long)rand() << 32`.

Since the binary can write however many 8-byte elements into the stack array, we can overwrite the return address, use ROP chains etc.
Howerver, the binary also uses stack canaries.
When writing data to the stack array, we inevitably have to overwrite the canary, which is equivalent to the 18th element of this array.

## Stage 1: Leak the canary
This step is actually the most interesting one.
Leaking the canary is rather simple: we just tell the program that `num` is 18, and write `0` 17 times so that the binary prints `canary ^ random_number`.

Now we need to guess this random number.
For this, we can make our own program which prints a 64-bit random number that's genrated in the same way in which `sum_encryption` does it.
The program that does this is [`get_rand.c`](./get_rand.c).
The trick here is to start both the remote process and the local one **at roughly** the same second since Epoch.
The reason for this is that `time` outputs the time in seconds since Epoch.
If we manage to call `srand` with the same seed twice, it will generate the same random numbers, since it's merely a PRG.
We use the random number printed by `get_rand` to xor the output received from the server and obtain the canary.

## Steps 2 + 3: Leak the address of `puts` and call `system("bin/sh")`
The next 2 steps are identical to almost every other challenge in this assignment.
The only difference is that now we write each 8-byte value on the stack individually instead of passing all of them in a single payload.

**Note:** In order to run the exploit properly, run the `exploit.sh` script.
