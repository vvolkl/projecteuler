	.file	"e001.f90"
	.section	.rodata
	.align 8
.LC0:
	.string	"/home/vali/Repos/projecteuler/e001.f90"
	.text
	.type	MAIN__, @function
MAIN__:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$496, %rsp
	movl	$0, -8(%rbp)
	movl	$1, -4(%rbp)
	cmpl	$999, -4(%rbp)
	jg	.L2
.L3:
	movl	-8(%rbp), %edx
	movl	-4(%rbp), %eax
	addl	%edx, %eax
	movl	%eax, -8(%rbp)
	cmpl	$999, -4(%rbp)
	sete	%al
	movzbl	%al, %eax
	addl	$1, -4(%rbp)
	testl	%eax, %eax
	jne	.L2
	jmp	.L3
.L2:
	movq	$.LC0, -488(%rbp)
	movl	$11, -480(%rbp)
	movl	$128, -496(%rbp)
	movl	$6, -492(%rbp)
	leaq	-496(%rbp), %rax
	movq	%rax, %rdi
	call	_gfortran_st_write
	leaq	-8(%rbp), %rcx
	leaq	-496(%rbp), %rax
	movl	$4, %edx
	movq	%rcx, %rsi
	movq	%rax, %rdi
	call	_gfortran_transfer_integer_write
	leaq	-496(%rbp), %rax
	movq	%rax, %rdi
	call	_gfortran_st_write_done
	movl	$0, %esi
	movl	$0, %edi
	call	_gfortran_stop_string
	.size	MAIN__, .-MAIN__
	.globl	main
	.type	main, @function
main:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$16, %rsp
	movl	%edi, -4(%rbp)
	movq	%rsi, -16(%rbp)
	movq	-16(%rbp), %rdx
	movl	-4(%rbp), %eax
	movq	%rdx, %rsi
	movl	%eax, %edi
	call	_gfortran_set_args
	movl	$options.1.3391, %esi
	movl	$9, %edi
	call	_gfortran_set_options
	call	MAIN__
	movl	$0, %eax
	leave
	ret
	.size	main, .-main
	.section	.rodata
	.align 32
	.type	options.1.3391, @object
	.size	options.1.3391, 36
options.1.3391:
	.long	68
	.long	1023
	.long	0
	.long	0
	.long	1
	.long	1
	.long	0
	.long	0
	.long	31
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.10) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
