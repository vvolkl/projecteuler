.FORMATSTR:
        .string "%d\n"
.META:
        .text
        .globl	main
        .type	main, @function
main:                                 # int main() {
        pushq   %rbp									# ...
        movq    %rsp, %rbp						# ...
        subq    $16, %rsp							# ...
        movl    $0, -4(%rbp)					# int result = 0;
        movl    $0, -8(%rbp)					# int i = 0;
.LOOP1:
        cmpl    $999, -8(%rbp)        # i < 999
        jg      .PRINT								# ...
        movl    -8(%rbp), %eax        # do something in the loop  
        addl    %eax, -4(%rbp)        # for example: result += i;
        addl    $1, -8(%rbp)          # i++;
        jmp     .LOOP1
.PRINT:
        movl    -4(%rbp), %eax				# printf("%d\n",result);
        movl    %eax, %esi						# ...
        movl    $.FORMATSTR, %edi			# ...
        movl    $0, %eax							# ...
        call    printf								# return 0;
        movl    $0, %eax							# ...
        leave													# ...
        ret														# ...
