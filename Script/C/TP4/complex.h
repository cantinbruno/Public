#include <stdio.h>
#include <math.h> /* -lm option */
#define __OPE_PLUS__ '+'
#define __OPE_LESS__ '-'


typedef struct complex {
    
    int a;
    int b;
}
Complex;


Complex new_complex(int a, int b);

void print_complex(Complex compl);

Complex sum(Complex compl1, Complex compl2);

Complex conjuguate(Complex compl);

int norm(Complex compl);