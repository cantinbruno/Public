#include <stdio.h>
#include <stdlib.h>


void ask_a_number(int * x, int indice) {
    
    fprintf(stdout, "Entrez un %d eme nombre :\n$> ", indice);
    scanf("%d", x);
}


void print_invert_number(int x, int n) {
    
    int p, q;
    p = x / n;
    q = x % n;

    while (a != p) {
        print_invert_number(q, n / 10);
    }
    fprintf(stdout, "%d", p);
}

int unity(int x) {
    
    int i;
    if (x < 10) return 1; 
    for (i = 1; i < (x / i) ; i *= 10) {
        ;
    }
    return i;
}

int main(int argc, char * argv[]) {
    
    int a;

    fprintf(stdout, "$> EXERCICE 3\n");

    if (argc < 2) {
        
        fprintf(stdout, "$> you can also run with argument like this :: \n");
        fprintf(stdout, "$> %s [a]\n", argv[0]);

        ask_a_number(&a, 1);

    }
    else {
        /*a = atoi(argv[1]);*/
        sscanf(argv[1], "%d", &a);
        
    }

    print_invert_number(a, unity(a));
    fprintf(stdout, "\n");
    
    return 0;
}