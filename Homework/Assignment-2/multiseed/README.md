# Multiseed
Were you running out of ideas or what?
This task literally means copy-pasting from Ghidra.
Not cool...

So what program does is it wants to receive the flag as a CLI parameter.
Then it spawns 10 threads.
Each of them receives a seed.
This seed is used by each thread to generate 41 (41 being the length of the flag) random numbers.
Each of these random numbers is xored with one of the bytes from the flag given as input to the program.
The result of these `xor`ed strings are kept on the stack of each thread

Each thread returns whether the resulting `xor`ed strings are the same as `flag_enc`, which, supposedly, holds... the encrypted flag.
So, in short, each threads checks whether its seed is the one that generated `flag_enc`, provided you provide the correct flag as input to the program.
Kind of lame.

The way to get the flag was to copy-paste `flag_enc` and the secrets from the binary into another .c file, together with the code that generates the random numbers.
Then, I iterated through all seeds and tried to xor `flag_enc` with the resulting randoms.
The correct seed turned out to be 1833309849.

![Oh, Weak](https://c.tenor.com/YAW8A9llaHAAAAAi/oh-weak-eric-cartman.gif)