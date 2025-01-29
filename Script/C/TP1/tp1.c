#include <stdio.h>
#include <stdlib.h>
#include "tp1.h"


int add(int a, int b) {

    return a + b;
}


void add_and_print(int a, int b) {
    
    fprintf(stdout, ">>> %d + %d = %d\n", a, b, add(a, b));
     
}


int fact(int n) {
    
    if (n < 1) {
        return 1;
    }
    return n * fact(n - 1);
}

int expo(int a, int b) {
    
    if (b == 0) {
        return 1;
    }
    return a * expo(a, b - 1);
}


void print_n_char(char c, unsigned int a) {
    
    if (a > 0) {
        fprintf(stdout, "%c", c);
        print_n_char(c, a - 1);    
    }
}


void pyra_dec(int n, char c) {
    
    int i;
    for (i = n; i > 0; i--) {
        print_n_char(c, i);
        printf("\n");
    }
}


void pyra_inc(int n, char c) {
    
    int i;
    for (i = 0; i < n; i++) {
        print_n_char(c, i);
        printf("\n");
    }
}


void pyra_entire_rec(int n, int i, char c) {
    
    if (n == i) {
        return ;
    }
    print_n_char(' ', n - i);
    print_n_char(c, 2 * i + 1);
    printf("\n");
    pyra_entire_rec(n, i + 1, c);
}


void pyra(int n) {
    
    pyra_entire_rec(n, 0, '*');
}


int fact_iter(int n) {
    
    int i, res;
    res = 1;
    for (i = 1; i <= n; i++) {
        res *= i;
    }
    return res;
}

int expo_iter(int a, int b) {

    int i, res;
    res = a;
    for (i = 1; i < b; i++) {
        res *= a;
    }
    return res;
}

void print_n_char_iter(char c, unsigned int a) {
    
    unsigned int i; 
    for (i = 0; i < a; i++) {
        fprintf(stdout, "%c", c);
    }
}

void pyra_entire_iter(int n, char c) {
    
    int i;
    for (i = 0; i < n; i++) {
        print_n_char(' ', n - i);
        print_n_char(c, 2 * i + 1);
        printf("\n");
    }
}
