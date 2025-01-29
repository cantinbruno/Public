#include <stdio.h>
#include <stdlib.h>
#define TAILLE 12

/*
    Ce programme essaye de copier un tableau d'entiers et de l'afficher 

    Ce programme ne compilera pas car dans la fonction
    creer_entiers, on essaye de renvoyer l'adresse d'une variable local
    qui ne sera plus défini après le scope, on aura donc une erreur de segmentation.  
*/

void affiche_tab(int* tab, int taille) {
    
    int i;
    for(i=0;i<taille;i++)
        printf("%d ",tab[i]);
    printf("\n");
}



int * creer_entiers() {
    int i;
    int * tab = (int *) malloc(sizeof(int) * TAILLE);
    for(i=0;i<TAILLE;i++)
        tab[i]=i+1;
    return tab;
}

int main() {
    int copy[TAILLE];
    int* tab = creer_entiers();
    
    int i;
    for(i=0;i<TAILLE;i++)
        copy[i] = tab[i];
    affiche_tab(copy,TAILLE);
    affiche_tab(tab,TAILLE);
    
    free(tab);
    return 0;
}
