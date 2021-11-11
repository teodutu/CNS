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
