#include <stdio.h>

#define M 1000000007

int main()
{
    int N;
    scanf("%d", &N);

    long long result = 1;
    for(int i = 1; i < 10; i++) {
        result *= N + i;
        result %= M;
    }
    result *= 831947206;
    result %= M;

    printf("%d\n", (int)result);

    return 0;
}
