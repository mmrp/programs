#include <stdio.h>
#ifdef DEBUG
#define dprintf(...) printf(__VA_ARGS__)
#else
#define dprintf(...) 
#endif

int solve(int n, int arr[], int l)
{
    long long m, p;
    int c, i, j;
   
    p = n;
    for (i = 1; i < ((1<<l)-1); i++) {
        m = 1;
        c = 0;
        j = i;
        while (j) {
            int pos;
            pos = ffsl(j);
            dprintf("pos = %d\n", pos);
            m *= arr[pos-1];
            j = j & (j-1); 
            c++;
        }
        if (c&1) 
            p -= n/m;
        else
            p += n/m;
        dprintf("%lld\n", m);
    }
    printf("%lld\n", p);
}

int main()
{
    int t, n;
    int arr[]= {2,3,5};
    scanf("%d", &t);
    while (t--){
        scanf("%d", &n);
        solve(n, arr, 3);
    }
    return 0;
}

