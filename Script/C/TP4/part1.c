#include <stdio.h>
#include <stdlib.h>

#define __NB_HOURS__ 24
#define __NB_SECONDS__ 60

#define __MIN_IN_SEC__ __NB_SECONDS__
#define __HOURS_IN_SEC__ (__NB_SECONDS__ * __NB_SECONDS__)
#define __DAYS_IN_SEC__ (__HOURS_IN_SEC__ * __NB_HOURS__)



void print_time(int seconds);


void print_time(int seconds) {
    
    int sec, min, hours, days;
    days = seconds / __DAYS_IN_SEC__;
    hours = (seconds % __DAYS_IN_SEC__) / __HOURS_IN_SEC__;
    min = (seconds % __HOURS_IN_SEC__) / __MIN_IN_SEC__;
    sec = seconds % __MIN_IN_SEC__;
    fprintf(stdout, "clock :: %02d:%02d:%02d:%02d\n", days, hours, min, sec);
}


int count_string(char * string) {
    
    int i, count;
    for (i = 0, count = 0; string[i] != '\0'; i++) {
        count += string[i];
    }
    return count;
}


int input_tab(int n, int tab[]) {
    
    int i;
    for (i = 0; i < n; i++) {
        fscanf(stdin, "%d", &tab[i]);
    }
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

int main(int argc, char * argv[]) {

    int input, res;
    int tab[] = {0, 0, 0, 0};
    if (argc < 2) {
        return 1;
    }
    input_tab(4, tab);
    print_tab(4, tab);
    /*input = atoi(argv[1]);
    print_time(input);*/
    /*res = count_string(argv[1]);
    fprintf(stdout, "count string :: %s :: %d\n", argv[1], res);*/
    return 0;
}