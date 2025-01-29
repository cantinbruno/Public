#include <stdio.h>
#include <stdlib.h>

#include "tp1.h"


int main(int argc, char * argv[]) {
    

    int a, b;
    if (argc < 3) {
        fprintf(stdout, "%s [a] [b]\n", argv[0]);
        return 1;
    }
    
    a = atoi(argv[1]);
    b = atoi(argv[2]);

    fprintf(stdout, "add :: %d\n", add(a, b));
    add_and_print(a, b);
    fprintf(stdout, "fact :: %d\n", fact(a));
    fprintf(stdout, "expo :: %d\n", expo(a, b));
    
    fprintf(stdout, "fact_iter :: %d\n", fact_iter(a));
    fprintf(stdout, "expo_iter :: %d\n", expo_iter(a, b));
    
    
    pyra(a);

    return 0;
}