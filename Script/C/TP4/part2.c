#include <stdio.h>




int swap(int * a, int * b) {
    
    int tmp;
    tmp = *a;
    *a = *b;
    *b = tmp;
    return 1;
} 

int swap_tab(int i1, int i2, int * tab) {
    
    swap(&tab[i1], &tab[i2]);
    swap(tab + i1, tab + i2);
    return 1;
}


int print_tab(int n, int tab[]) {

    int i;
    fprintf(stdout, "[ ");
    for (i = 0; i < n; i++) {
        fprintf(stdout, "%d, ", tab[i]);
    }
    fprintf(stdout, "]\n");
    return 1;
}

int main(void) {
    int a, b;
    int tab[] = {0, 2, 4, 6, 8};
    a = 3;
    b = 4;
    fprintf(stdout,"a = %d, b = %d\n", a, b);
    swap(&a, &b);
    fprintf(stdout,"a = %d, b = %d\n", a, b);
    swap_tab(0, 3, tab);
    print_tab(5, tab);
    return 0;
}