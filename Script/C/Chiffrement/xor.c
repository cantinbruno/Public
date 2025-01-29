#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[]) {
    int b1, b2;
    FILE *a1 = fopen(argv[1], "rb");
    FILE *a2 = fopen(argv[2], "rb");
    while ((b1 = fgetc(a1)) != EOF && (b2 = fgetc(a2)) != EOF) {
        putchar(b1 ^ b2);
    }
    fclose(a1);
    fclose(a2);
    return 1;
}
