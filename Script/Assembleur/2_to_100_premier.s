.data
str:    .asciz "x=%d \n"
.text
.global main
main:
    movl    %esp,   %ebp #correct debug
    movl    $2, %edi
    
boucle:
    incl    %edi
    cmpl    $100,   %edi
    jg      fin_boucle
    
    movl    $2, %ecx
   
boucle2:
    cmpl    %edi,   %ecx
    jge     fin_boucle2
    xorl    %edx,   %edx
    movl    %edi,   %eax
    idivl   %ecx
    cmpl    $0, %edx
    je      boucle
    incl    %ecx   
    jmp     boucle2
    
fin_boucle2:   
    pushl   %edi
    pushl   $str
    call    printf
    addl    $8, %esp
    
    incl    %edi
    jmp     boucle
    
fin_boucle:
    xorl    %eax,   %eax
    ret
