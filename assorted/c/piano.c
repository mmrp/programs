#include <stdio.h>
#include <string.h>

#ifdef DEBUG
#define dprintf(...) printf(__VA_ARGS__)
#else
#define dprintf(...) 
#endif
#define MAX_MARK 1000010
#define TPRIMES    78600

long long primes[TPRIMES];
char mark[MAX_MARK]; 
int last_prime_index;

#define MAX_N_FACTOR 42
int factor[MAX_N_FACTOR];
int power[MAX_N_FACTOR];

void gen_primes() 
{ 
    long long i, j, k; 

    for (i = 1; i < MAX_MARK; i++) 
        mark[i] = 1; 

    for(i = 2, k = 0; i <= MAX_MARK; i++) {
        if (mark[i]) {
            primes[k++] = i;
            for(j = i; j*i < MAX_MARK; j++) 
                mark[i*j] = 0; 
        }
    }
    last_prime_index = k;
} 

void find_factors(long long num, int fac[], int pow[])
{
    int i, j, k;
    int p;

    memset(fac, 0, sizeof(fac));
    memset(pow, 0, sizeof(pow));

    k = 0;
    for (i = 0, p = primes[k]; ((p*p) < num) && (k < last_prime_index); p = primes[++k]) {
        if (num % p == 0) {
            fac[i] = p;
            do {
                num /= p;
                pow[i]++;
            } while (num % p == 0);
            i++;
        }
    }
    if (num > 1) {
        fac[i] = num;
        pow[i] = 1;
        i++;
    }

    for (j = 0; j < i; j++) {
        printf("%5lld: %5lld\n", fac[j], pow[j]);
    }
}

long long pisano(long long M)
{
    long long p;

    if (m == 1)
        return 1;

    if (mark[m]) {
        p = m;
        if (p == 2)
            return 3;
        if (p == 5)
            return 20;
    }


}

int main()
{
    int t;
    long long M;

    gen_primes();
    
    printf("Last prime = %d\n", primes[last_prime_index-1]);

    scanf("%d", &t);
    while (t--) {
        scanf("%lld", &M);
        find_factors(M, factor, power);
        pisano(M);
    }
    return 0;
}

