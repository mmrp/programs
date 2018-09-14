#include <stdio.h>
#include <string.h>

#ifdef DEBUG
#define dprintf(...) printf(__VA_ARGS__)
#else
#define dprintf(...) 
#endif
#define MAX_ELEM 51
#define MAX_SUM  (17*51) //(51*51/3)
char D[MAX_SUM][MAX_SUM][2];
int A[MAX_ELEM];


int find_partition(int E[], int N, int S)
{
    int x, y, k, d, e, v;
    int p1, p2;
    //base case
    D[0][0][0] = 1;
    p1 = 1;
    p2 = 0;
    for (k = 1; k <= N; k++) {
        dprintf("k = %d\n", k);
		p1 = 1 - p1;
		p2 = 1 - p2;
        for (x = 0; x <= S; x++) {
            for (y = 0; y <= x; y++) {
                v = D[x][y][p1];
				if (!v) {
					d = x - E[k];
					if (d >= 0) {
						if (d < y)
							v |= D[y][d][p1];
						else
							v |= D[d][y][p1];
					}
					e = y - E[k];
					if (e >= 0)
						v |= D[x][e][p1];
				}
				D[x][y][p2] = v;
				dprintf("%d ", D[x][y][p2]); 
			}
			dprintf("\n");
		}
	}
	return D[S][S][p2];
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
        if (sum % 3 == 0) {
            memset(D, 0, sizeof(D));
            res = find_partition(A, N, sum/3);
        }

        if (res) 
            printf("Case %d: Happy Eid Day\n", c);
        else
            printf("Case %d: Lov-e Pap Pap-e Polti\n", c);
        c++;
    }
    return 0;
}
