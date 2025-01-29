#include <stdio.h>
#include <stdlib.h>

#include "tp2.h"


int somme(int a, int b) {
    
    int i, res;
    for (i = a, res = 0; i <= b; i++) {
        res += i;
    }
    return res;
}

void ask_a_number(int* x, int indice) {
    
    fprintf(stdout, "$> Entrez un %d eme nombre :\n$> ", indice);
    scanf("%d", x);
}


int main(int argc, char * argv[]) {
    
    int i;
    int tab[2];

    fprintf(stdout, "$> EXERCICE 2\n");

    for (i = 1; i < argc; i++) {

        /*tab[i - 1] = atoi(argv[i]);*/
        sscanf(argv[i], "%d", &tab[i - 1]);
    }
    if (argc < 3) {
        
        fprintf(stdout, "$> you can also run with argument like this :: \n");
        fprintf(stdout, "$> %s [a] [b]\n", argv[0]);

        for (i = argc; i < 3; i++) {
            ask_a_number(&(tab[i - 1]), i);
        }
    }
    fprintf(stdout, "$> Somme %d %d :: %d\n", tab[0], tab[1], somme(tab[0], tab[1]));

    return 0;
}
