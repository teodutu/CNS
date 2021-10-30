extern printf

SECTION .rodata
; message format for printf() call
message: db "Sum(%d) is %d", 10, 0
msg_to_user: db "Type a number: ", 0
int_fmd: db "%d", 0

SECTION .bss
; number to get the sum to
num: resd 1


SECTION .text
extern printf
extern scanf
global main

main:
	push rbp
	mov rbp, rsp

	; Use eax to compute sum. Sum is initially 0.
	xor rax, rax	; sum is initially 0

	mov rdi, msg_to_user
	call printf

	mov rsi, num
	mov rdi, int_fmd
	call scanf

	; Use ecx as loop counter. Start from num and decrement to 0.
	mov rcx, [num]
compute_sum_loop:
	; For each step add current counter (ecx) to sum (eax).
	add rax, rcx
	loop compute_sum_loop

    ; Move arguments to registers (rdi = format, rsi = num, rdx = sum)
	; and call printf.
	mov rdx, rax
	mov rdi, message
	mov rsi, [num]
	call printf

	leave
	ret
