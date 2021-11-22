# `call_me_arm`
I tried to approach this binary the same way I did `call_me_reloaded`.
This meant writing a `call call_me` (`bl call_me`) at the end of `main` and then set `call_me`'s parameters accordingly.
I decompiled the binary using Ghidra and I noticed it's the same scenario as with `call_me_reloaded`:
- `r0` needs to be `0x1337`;
- `r1` needs to be a string whose first 3 characters are `CNS`.

## `bl call_me`
In order to call the function, I drew inspiration from the instruction below, from where I deduced that the offset in the opcode is the difference of the addresses **divided by 4**.
It's probably an optimisation thanks to the fact that all `arm7l` instrucions are 4 bytes long.
```
105a4:	ebffffe2 	bl	10534
```

Thus, I needed to get to address `0x10604`, starting from `0x10734` (same as with `call_me`, the offset is calculated form the address of the next instruction after `call`, beause pipelining).
This means a differnece of `0x130` bytes, which means an offset of `0x130 / 4 = 0x4c`.
So the opcode will contain: `0xffffff - 0x4c = 0xffffb3`.

## The arguments of `call_me`
In order to assemble all `mov`s, I used [shell-storm.org](http://shell-storm.org/online/Online-Assembler-and-Disassembler/).

The first argument was simple: `mov r0, #4919`.

For the second parameter, I looked for `CNS` in the binary using `xxd` and I found it at offset `0x748`, which, at runtime, becomes address `0x10748`.
How convenient that the string is placed right after the `main` funcion?
But now came a problem caused by the address of the string, which was too large to be stored in `r1` with a single instruction.
So I did what everyone does and I _googled_ it.
And I found this [trick](https://stackoverflow.com/a/41470140).
Thus, I loaded the "low" bytes (`0x748`) into `r1` using `movw` and the "high" ones (merely `0x1`) with `movt`.

![Outstanding Move](https://i.kym-cdn.com/entries/icons/original/000/027/838/Untitled-1.jpg)

However, this took 4 instructions, so I was forced to replace the `call close` mnemonic with `movw r0, #4919`.
But this is no big deal.
The OS closes all file descriptors when the process ends, anyway...

## Results
In the end, the resulting code looks like this:
```asm
10724:	e3010337 	movw	r0, #4919	; 0x1337
10728:	e3001748 	movw	r1, #1864	; 0x748
1072c:	e3401001 	movt	r1, #1
10730:	ebffffb3 	bl	10604 <call_me>
```
