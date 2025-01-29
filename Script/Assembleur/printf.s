.data
str: .asciz "L’assembleur est cool ! \n"
.text
.global main
main:
pushl %ebp
movl %esp, %ebp
pushl $str
call printf
leave
ret
