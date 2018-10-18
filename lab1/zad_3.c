#include <stdio.h>
#include <gsl/gsl_ieee_utils.h>

void print_iteration(int i)
{
    printf("Iteration ");
    char c100 = ' ', c10 = ' ', c1 = i % 10 + '0';
    if (i >= 10)
        c10 = (i/10) % 10 + '0';
    if (i >= 100)
        c100 = (i/100) % 10 + '0';
    printf("%c%c%c:   ", c100, c10, c1);
}

int main()
{
    float f = 1.0;
    for (int i = 0; i < 160; i++) {
        print_iteration(i);
        gsl_ieee_printf_float(&f);
        printf("\n");
        f /= 2.0;
    }
    return 0;
}