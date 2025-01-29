#include <stdio.h>
#include "complex.h" 



int main(void) {
    
    Complex compl1, compl2;
    Complex conjugue, complsum;

    compl1 = new_complex(2, 4);
    compl2 = new_complex(3, 5);
    conjugue = conjuguate(compl1); 
    complsum = sum(compl1, compl2); 

    print_complex(compl1);
    print_complex(compl2);
    print_complex(conjugue);
    print_complex(complsum);
    
    fprintf(stdout,"module :: %d\n", norm(compl1));

    return 0;
}