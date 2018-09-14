#include <stdio.h>
#ifdef DEBUG
#define dprintf(...) printf(__VA_ARGS__)
#else
#define dprintf(...) 
#endif

#define MAX_ELEM 1000000+10
long long modulus=1000000007;
long long fact[MAX_ELEM];
long long ifact[MAX_ELEM];

long long  power_mod(long long a, long long p, int m)
{
    long long c = 1;
    while (p) {
        if (p&1) 
            c = (c * a) % m;
        a = (a * a) % m;
        p = p >> 1;
    }
    return c;
}

void calculate_factorials()
{
    long long  i;
    fact[0] = 1;
    for (i = 1; i < MAX_ELEM; i++) {
        fact[i] = (i * fact[i-1]) % modulus;
    }
    ifact[0] = 1;
    ifact[1] = 1;
    for (i = 2; i < MAX_ELEM; i++) {
        ifact[i] = (power_mod(i, modulus-2, modulus) * ifact[i-1]) % modulus;
    }
}
long long comb(int n, int r)
{
    printf("%lld %lld\n", fact[n], ifact[r]);
    return (fact[n] * ifact[r])% modulus;
}
int main()
{
    int t;
    long long r;
    scanf("%lld", &r);
    calculate_factorials();
    printf("%lld\n", comb(100, r));
    return 0;
}

