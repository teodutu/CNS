# CNS
Computer and Network Security - UPB 2021-2022 - https://ocw.cs.pub.ro/courses/cns



## Labs
### Lab 1 - Introduction
Basic tools such as `strace`, `ltrace`, `strings` or `objdump`.
Not included because too easy.


### Lab 2 - Program Analysis
Mainly the analysis of ELF headers, sections an segments.
Only 2 tasks are included because the rest are either stupid or uninteresting.


### Lab 3 - Buffer Overflow
A few scenarios where buffer overflows could be exploited.
Basically IOCLA.


### Lab 4 - Shellcodes 1
Tutorials and introductory shellcodes tasks.
Meant to be solved by manually writing shellcodes...
`pnwtools` go brrrrrr.


### Lab 5 - Shellcodes 2
Only 2 tasks:
- an `env`-based exploit, where the shellcode is stored in an environment variable;
- a disgusting command interpreter where you leak the address of a buffer and then use a 2-stage attack to open a shellcode.


### Lab 6 - Exploit Protection Mechanisms
This lab is about bypassing ASLR on 32-bit binaries by bruteforce (the good old way).
The lab is also about bypassing stack canaries given an unsanitised `read`, whose buffer is `printf`'d without a trailing `\0`.
This `printf` method is also used to leak the address of the environment variable `SHELLCODE`, which is used to pass ... well, a shellcode to the binary.


### Lab 7 - String attacks
Tasks 0-3 are decent and are either simple information leaks or `%n` arbitrary memory writes.
Task 4 is a disgusting mess, which _should_ work in theory, but doesn't in practice.
It's also hard to debug, because the bug happens somewhere inside `printf` (it tries to perform a memory write at an incorrect address...).


### Lab 8 - ROP
ROPs are used to chain function calls and to perform a `ret-2-libc` attack in order to call `read` for reading a shellcode into a data section buffer, then run `mprotect(R | X)` on that buffer, before finally jumping into it.


### Lab 9 - ROP + Stack Pivoting
Theoretically, this lab is about stack pivoting.
However, neither task even requires ROPs.
The functions can be exploited by jumping inside them, after the parameters are checked.
Obviously, since not even ROPs are necessary to solve the challenges, stack pivoting is even more overkill.
Not cool.



## Homework
### Assignment 1
Honestly, the tasks are disgusting as all of them bar one (`crypto`) involve reversing and patching binaries.
No overflows, no shellcodes, nothing interesting.
And `crypto` is only cool because we're supposed to figure out the cipher is RC4.
There's still hope for better 2nd and 3rd assignments.
