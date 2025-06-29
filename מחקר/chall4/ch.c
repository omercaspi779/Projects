#include <stdio.h>

typedef struct {
    char a[10];
    char b[10];
    char c[10];
    char flag[5];
} object;

int main() {
    printf("%lu\n", sizeof(object));
}
