#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "tp2.h"


void print_numbers_for(int a, int b, int step) {
    
    int i, cmpt, incr;

    incr = (b < a) ? 1 : - 1;
    for (i = b, cmpt = 1; i != a; i = i + incr, cmpt++) {

        fprintf(stdout, "%d ", i);
        (cmpt == step) ? cmpt = 0, fprintf(stdout, "\n") : 0;
    }
    fprintf(stdout, "%d\n", i);
}


void print_numbers_while(int a, int b, int step) {
    
    int i, cmpt, incr;

    i = b; cmpt = 1;
    incr = (b < a) ? 1 : - 1;
    
    while (i != a) {

        fprintf(stdout, "%d " , i);
        (cmpt == step) ? cmpt = 0, fprintf(stdout, "\n") : 0;
        i = i + incr; cmpt++;
    }
    fprintf(stdout, "%d\n", i);
}



void print_numbers_to_ten(int step) {
    
    print_numbers_while(1, 10, step);
}

void print_numbers(int a, int b, int step) {

    print_numbers_while(a, b, step);
}


void ask_a_number(int * x, int indice) {
    
    fprintf(stdout, "Entrez un %d eme nombre :\n$> ", indice);
    scanf("%d", x);
}


int main(int argc, char * argv[]) {
    
    int i;
    int tab[3];

    fprintf(stdout, "$> EXERCICE 1 \n");

    for (i = 1; i < argc; i++) {

        /*tab[i - 1] = atoi(argv[i]);*/
        sscanf(argv[i], "%d", &(tab[i - 1]));
    }
    if (argc < 4) {
        
        fprintf(stdout, "$> you can also run with argument like this :: \n");
        fprintf(stdout, "$> %s [a] [b] [c]\n", argv[0]);

        for (i = argc; i < 4; i++) {
            ask_a_number(&tab[i - 1], i);
        }
    }
    print_numbers_to_ten(tab[2]);
    print_numbers(tab[0], tab[1], tab[2]);

    return 0;
}

