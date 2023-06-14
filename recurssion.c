#include <stdio.h>

int factorial(int n)
{
    if (n == 1)
        return 1;
    return n * factorial(n - 1);
}

int main()
{
    int fact = factorial(5);
    printf("Factorial: %d\n", fact);
    return 0;
}