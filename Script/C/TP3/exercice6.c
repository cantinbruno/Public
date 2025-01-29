#include <stdio.h>

/*
    Ce code affiche les entiers de 1 à 12
*/
/*
    Le warning concerne la ligne 19, car ici on déclare à la compilation un 
    tableau d'entiers de taille variable, (ici on devrait plutot faire un malloc)  
*/

void affiche_tab(int* tab, int taille) {
    
    int i;
    for(i=0;i<taille;i++)
        printf("%d ",tab[i]);
    printf("\n");
}

void affiche_entiers(int n) {
    int tab[n];
    int i;
    for(i=0;i<n;i++)
        tab[i]=i+1;
    affiche_tab(tab,n);
}

int main() {
    affiche_entiers(12);
    return 0;
}