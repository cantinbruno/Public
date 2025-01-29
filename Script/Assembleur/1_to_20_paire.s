.data
str:    .asciz "x=%d \n"
.text
.global main
main:
    movl    %esp,   %ebp #correct debug
    movl    $1, %edi
boucle:
    incl    %edi
    cmpl    $20,   %edi
    jg      fin_boucle
    movl    %edi, %eax
    andl    $1, %eax
    jnz     boucle
    
    pushl   %edi
    pushl   $str
    call    printf
    addl    $8, %esp
    
    incl    %edi
    jmp     boucle
    
fin_boucle:

    xorl    %eax,   %eax
    ret