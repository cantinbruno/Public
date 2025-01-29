#include <stdio.h>
#include "complex.h"


Complex new_complex(int a, int b) {
    
    Complex compl;
    compl.a = a;
    compl.b = b;
    return compl;
}

void print_complex(Complex compl) {
    
    char ope, b;
    ope = (compl.b > 0) ? __OPE_PLUS__ : __OPE_LESS__; 
    b  = (compl.b < 0) ? compl.b * (-1) : compl.b;
    fprintf(stdout, "Complex:: %d %c i%d\n", compl.a, ope, b);
}

Complex sum(Complex compl1, Complex compl2) {
    
    Complex sumof;
    sumof.a = compl1.a + compl2.a;
    sumof.b = compl1.b + compl2.b;
    return sumof;
}

Complex conjuguate(Complex compl) {

    Complex conjugue;
    conjugue.a = compl.a;
    conjugue.b = - compl.b;
    return conjugue;
}

int norm(Complex compl) {
    
    int a, b, module;
    a = compl.a * compl.a;
    b = compl.b * compl.b;
    module = sqrt(a + b);
    return module;
}