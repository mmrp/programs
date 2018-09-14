#include <stdio.h>
#include <string.h>

#ifdef DEBUG
#define dprintf(fmt, ...) do { printf(fmt, __VA_ARGS__); } while (0)
#else
#define dprintf(fmt, ...) 
#endif

#define MAX_N 60
#define MAX_S 125250
//char arr[MAX_N * MAX_S];
int  lpos[(MAX_N)*(MAX_N)];
int  arr1[MAX_N], arr2[MAX_N];
int  skip[MAX_N];


int find_sum(int arr[], int N, int sum)
{
    int s, p, ts;
    int k;
    lpos[0] = 0;
    for (s = 0; s <= sum; s++) {
        lpos[s] = -1;
        for (p = 0; p < N; p++) {
            ts = s - arr[p];
            if ((ts >= 0)) {
                if (ts == 0 || ((lpos[ts] != -1) && (lpos[ts] <= (p-1)))) {
                    lpos[s] = p;
                    dprintf("%d: %d, %d\n", s, p, arr[p]); 
                    break;
                }
            }
        }
    }
    if (lpos[sum] != -1)  {
        /*unwrap*/
        ts = sum;
        k = 0;
        while (ts > 0) {
            dprintf("%d ", arr[lpos[ts]]);
            skip[lpos[ts]] = 1;
            ts = ts - arr[lpos[ts]];
        }
        //printf("\n");
        return 1;
    }
    return 0;
}

int main()
{
    int T, N, i, c;
    int s, sum;
    int ret;
    char ans1[]="Happy Eid Day";
    char ans2[]="Lov-e Pap Pap-e Polti";
    scanf("%d", &T);
    c = 1;
    while (T--) {
        memset(skip, 0, sizeof(skip));
        scanf("%d", &N);
        s = 0;
        for  (i = 0; i < N; i++) {
            scanf("%d", &arr1[i]);
            s += arr1[i];
        }
        ret = 0;
        if (s % 3 == 0) {
            sum = s/3;
            if (find_sum(arr1, N, sum)) {
                int k = 0;
                for (i = 0; i < N; i++) {
                    if (!skip[i])
                        arr2[k++] =arr1[i];
                }
                if (find_sum(arr2, k, sum)) 
                    ret = 1;
            }
        }
        if (ret) 
            printf("Case %d: %s\n", c, ans1);
        else
            printf("Case %d: %s\n", c, ans2);
        c++;
    }
    return 0;
}
