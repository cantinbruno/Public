#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

void ask_a_character(char * c, int n) {
    
    fprintf(stdout, "Char n° %d :\n", n);
    *c = '\n';
    for (; *c =='\n'; scanf("%c", c)) {
        ;
    }
}



/* 
    calculer upper : x  + ('A' - 'a');
*/
void alternate(char begin, char end) {
    
    int i;
    for (i = begin; i <= end; i++) {
        
        (i % 2 == 1) ? printf("%c", tolower(i)) : printf("%c", toupper(i));
    }
    for (i = begin; i >= end; i--) {
        
        (i % 2 == 1) ? printf("%c", tolower(i)) : printf("%c", toupper(i));
    }
    fprintf(stdout, "\n");
}


int main(int argc, char * argv[]) {
    
    int i;
    char tab[2];

    fprintf(stdout, "$> EXERCICE 4\n");

    for (i = 1; i < argc; i++) {

        tab[i - 1] = *(argv[i]);
    }
    if (argc < 3) {
        
        fprintf(stdout, "$> you can also run with argument like this :: \n");
        fprintf(stdout, "$> %s [c1] [c2]\n", argv[0]);

        for (i = argc; i < 3; i++) {
            ask_a_character(&(tab[i - 1]), i);
            /*printf("%d\n", i - 1);*/
        }
    }

    alternate(tab[0], tab[1]);
    
    return 0;
}