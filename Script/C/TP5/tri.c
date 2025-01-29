#include <stdio.h>
#include <stdlib.h>



void mirroir(int taille, int tab[]);

void print_tab(int taille, int tab[]);

void swap(int * a, int * b);

int place_premier(int tab[], int taille);

/* -- TRIS -- */

void tri_dicho_aux(int first, int taille, int tab[]);

void tri_dicho(int taille, int tab[]);

void tri_bulles(int taille, int tab[]);

void tri_rapide_aux(int taille, int first, int last, int tab[]);

void tri_rapide(int taille, int tab[]);

void tri_bulles_opti(int taille, int tab[]);



int main(int argc, char * argv[]) {

    int tab[] = {1, 2, 3, 4, 5};
    int randomtab[] = {12, 8, 24, 6, 10, -5, 7, 9};
    int randomtab2[] = {27, 9, 53, 12, -10, -5, 7, 4};
    int randomtab3[] = {47, 104, 1, -89, 63, 12, 7, 4};

    print_tab(5, tab);

    fprintf(stdout, "Miroir :: \n");
    mirroir(5, tab);
    print_tab(5, tab);

    fprintf(stdout, "tri dicho :: \n");
    print_tab(8, randomtab3);
    tri_dicho(8, randomtab3);
    print_tab(8, randomtab3);


    fprintf(stdout, "tri bulles ::\n");
    print_tab(8, randomtab2);    
    tri_bulles_opti(8, randomtab2);
    print_tab(8, randomtab2);    


    fprintf(stdout, "tri rapide :: \n");
    print_tab(8, randomtab);
    tri_rapide(8, randomtab);
    print_tab(8, randomtab);

    return 0;
}





void swap(int * a, int * b) {
    
    int tmp;
    tmp = *a;
    *a = *b;
    *b  = tmp;
}

void mirroir(int taille, int tab[]) {
    
    int i;
    for (i = 0; i < taille / 2; i++) {
        swap(&tab[i], &tab[taille - i - 1]);
    }
}

void print_tab(int taille, int tab[]) {
    
    int i;
    fprintf(stdout, "[");
    for (i = 0; i < taille; i++) {
        fprintf(stdout, " %d", tab[i]);
    }
    fprintf(stdout, " ]\n");
}

/* tri dichotomique */


int place_premier(int tab[], int taille) {

    int i, j, x, ppg;
    ppg = 0;
    x = tab[ppg];
    for (i = 1; i < taille; i++) {
        if (tab[i] > x) {
            ppg = i;
            break;
        }
    }
    for (j = ppg + 1; j < taille; j++) {
        if (tab[j] <= tab[ppg]) {
            swap(&tab[j], &tab[ppg]);
            ppg++;
        }
    }
    swap(&tab[ppg - 1], &tab[0]);
    return ppg - 1;
}






void tri_dicho_aux(int first, int taille, int tab[]) {
    
    int p;

    if (taille <= 1) {
        return;
    }
    p = place_premier(tab, taille);
    tri_dicho_aux(0, p - 1, tab);
    tri_dicho_aux(p + 1, taille - 1, tab);
}

void tri_dicho(int taille, int tab[]) {
    
    tri_dicho_aux(0, taille, tab);
}



void tri_bulles(int taille, int tab[]) {
    
    int i, j;
    for (i = 0; i < taille - 1; i++) {
        for (j = 0; j < taille - i - 1; j++) {

            if (tab[j] > tab[j + 1]) {
                swap(&tab[j], &tab[j + 1]);
            }
        }
    }
}

void tri_bulles_opti(int taille, int tab[]) {
    
    int i, j, is_sort;
    for (i = 0; i < taille - 1; i++) {

        is_sort = 1;
        for (j = 0; j < taille - i - 1; j++) {
            if (tab[j] > tab[j + 1]) {

                swap(&tab[j], &tab[j + 1]);
                is_sort = 0;
            }
        }
        if (is_sort) {
            return;
        }

    }
}

void tri_rapide_aux(int taille, int first, int last, int tab[]) {
    
    int pivot, i, j;
    
    if (first >= last) {
        return;
    }
    pivot = first;
    i = first;
    j = last;
    while (i < j) {
        while (tab[i] <= tab[pivot] && i < last) 
            i++;
        while (tab[j] > tab[pivot])
            j--;
        if (i < j)
            swap(&tab[i], &tab[j]); 
        
    }
    swap(&tab[pivot], &tab[j]);
    tri_rapide_aux(taille, first, j - 1, tab);
    tri_rapide_aux(taille, j + 1, last, tab);
}

void tri_rapide(int taille, int tab[]) {
    
    tri_rapide_aux(taille, 0, taille - 1, tab);
}