#include <stdio.h>
#include <stdlib.h>


int max_of_tab_int(int tab[], int taille);

int min_of_tab_int(int tab[], int taille);

void print_tab(int tab[], int taille);

void copy_tab_between2(int tab1[], int taille1, int tab2[], int taille2, int begin);

void copy_tab_between3(int tab1[], int taille1, int tab2[], int taille2, int tab3[], int taille3);

int stringlen(char * chaine);

int longer_prefix(char * chaine1, char * chaine2);


int max_of_tab_int(int tab[], int taille) {
    
    int i, max;
    for (i = 1, max = tab[0]; i < taille; i++) {
        max = (max < tab[i]) ? tab[i]: max;
    }
    return max;
}

int min_of_tab_int(int tab[], int taille) {
    
    int i, min;
    for (i = 1, min = tab[0]; i < taille; i++) {
        min = (min > tab[i]) ? tab[i]: min;
    }
    return min;
}

void print_tab(int tab[], int taille) {
    
    int i;
    
    printf("[ ");
    for (i = 0; i < taille; i++) {
        printf("%d ", tab[i]);
    }
    printf("]\n");
}


void copy_tab_between2(int tab1[], int taille1, int tab2[], int taille2, int begin) {
    
    int i, taille;

    taille = (taille1 > taille2) ? taille2 : taille1;
    for (i = begin; i < begin + taille; i++) {
        tab2[i] = tab1[i - begin];
    }
}

void copy_tab_between3(int tab1[], int taille1, int tab2[], int taille2, int tab3[], int taille3) {
    
    copy_tab_between2(tab2, taille2, tab1, taille1, 0);
    copy_tab_between2(tab3, taille3, tab1, taille1, taille2);
}


int stringlen(char * chaine) {
    
    int i;
    for (i = 0; chaine[i] != '\0'; i++) {
        ;
    }
    return i;
}

int longer_prefix(char * chaine1, char * chaine2) {
    
    int i;
    for (i = 0; chaine1[i] == chaine2[i]; i++) {
        ;
    }
    return i;
}



int main(void) {

    int tabint1[] = {2, 1, 6, 0, 4, 91, -5, 8, -30, 13, 3};
    int tabint2[] = {31, 0, 4, -7};
    int tabint3[] = {1, 4, 7, 0, -5, -98};

    char * chaine = "Bonjour";
    int n1 = 11;
    int n2 = 4;
    int n3 = 6;

    printf("tab 1 :");
    print_tab(tabint1, n1);

    printf("tab 2 :");
    print_tab(tabint2, n2);

    printf("tab 3 :");
    print_tab(tabint3, n3);


    printf("max : %d\n", max_of_tab_int(tabint1, n1));
    printf("max : %d\n", max_of_tab_int(tabint2, n2));
    printf("max : %d\n", max_of_tab_int(tabint3, n3));

    printf("chaine : %s\n", chaine);
    printf("strlen : %d\n", stringlen(chaine));


    
    /*copy_tab_between2(tabint1, n1, tabint2, n2, 0);


    printf("tab 2 :");
    print_tab(tabint2, n2);*/

    copy_tab_between3(tabint1, n1, tabint2, n2, tabint3, n3);
    printf("tab 1 :");
    print_tab(tabint1, n1);

    printf("longer_prefix between %s / %s : %d\n", 
        "avion", "aviation", longer_prefix("avion", "aviation"));
    
    return 0;
}