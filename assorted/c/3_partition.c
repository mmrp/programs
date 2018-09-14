#include <stdio.h>
#ifdef DEBUG
#define dprintf(...) printf(__VA_ARGS__)
#else
#define dprintf(...) 
#endif
#define MAX_ELEM 51
#define MAX_SUM  (17*51) //(51*51/3)
int D[MAX_SUM][MAX_SUM][MAX_ELEM];
int A[MAX_ELEM];


int find_partition(int E[], int N, int S)
{
    int x, y, k, d;
    //base case
    D[0][0][0] = 1;

    for (k = 1; k <= N; k++) {
        dprintf("k = %d\n", k);
        for (x = 0; x <= S; x++) {
            for (y = 0; y <= S; y++) {
                D[x][y][k] = D[x][y][k-1];
				if (!D[x][y][k]) { 
					d = x - E[k];
					if (d > 0) {
						D[x][y][k] |= D[d][y][k-1];
#if 0			
						if (d >= y)
							D[x][y][k] |= D[d][y][k-1];
						else
							D[x][y][k] |= D[y][d][k-1];
#endif
					}

					d = y - E[k];
					if (d > 0)
						D[x][y][k] |= D[x][d][k-1];
				}
				dprintf("%d ", D[x][y][k]); 

			}
			dprintf("\n");
		}
    }
    return D[S][S][N];
}

int main()
{
    int t, i, N, c, sum, res;
    c = 1;
    scanf("%d", &t);
    while (t--){
        scanf("%d", &N);
        sum = 0;
        for (i = 1; i <= N; i++) {
            scanf("%d", &A[i]);
            sum += A[i];
        }
        dprintf("sum = %d\n", sum);

        res = 0;
        if (sum % 3 == 0) 
            res = find_partition(A, N, sum/3);

        if (res) 
            printf("Case %d: Happy Eid Day\n", c);
        else
            printf("Case %d: Lov-e Pap Pap-e Polti\n", c);
        c++;
    }
    return 0;
}
