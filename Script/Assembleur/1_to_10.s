.data
str:    .asciz "x=%d \n"
.text
.global main
main:
    movl    %esp,   %ebp #correct debug
    movl    $0, %edi
boucle:
    cmpl    $10,   %edi
    jg      fin_boucle
    
    pushl   %edi
    pushl   $str
    call    printf
    addl    $8, %esp
    
    incl    %edi
    jmp     boucle
    
fin_boucle:

    xorl    %eax,   %eax
    ret