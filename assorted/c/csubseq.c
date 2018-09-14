#include <stdio.h>
#include <string.h>

#ifdef DEBUG
#define dprintf(fmt, ...) do { fprintf(stderr, fmt, __VA_ARGS__); } while (0)
#else
#define dprintf(fmt, ...) 
#endif

#define MAX_SIZE 60
int DP[MAX_SIZE][MAX_SIZE][MAX_SIZE][MAX_SIZE];

int max(int a, int b, int c, int d)
{
	int e, f;
	e = a > b? a: b;
	f = c < d? c: d;
	return (e > f? e: f);
}

int main()
{
	int i, j, k, m;
	int alen, blen, clen, dlen;
	int count;
	char A[MAX_SIZE], B[MAX_SIZE], C[MAX_SIZE], D[MAX_SIZE];

	scanf("%s", &A[1]);
	scanf("%s", &B[1]);
	scanf("%s", &C[1]);
	scanf("%s", &D[1]);
	alen = strlen(&A[1]);
	blen = strlen(&B[1]);
	clen = strlen(&C[1]);
	dlen = strlen(&D[1]);
	count = 0;
				
	for (i = 1; i <= alen; i++) {
		for (j = 1; j <= blen; j++) {
			for (k = 1; k <= clen; k++) {
				for (m = 1; m <= dlen; m++) {
					if ((A[i] == B[j]) && (B[i] == C[k]) && (C[k] == D[m])) {
						DP[i][j][k][m] = 1 + DP[i-1][j-1][k-1][m-1]; 
						count++;
						printf("match: %d, %d ,%d, %d\n", i, j, k, m);
					}
					else {
						DP[i][j][k][m] = max(DP[i-1][j][k][m], DP[i][j-1][k][m], DP[i][j][k-1][m], DP[i][j][k][m-1]);
					}
				}
			}
		}
	}
	printf("%d\n", DP[alen][blen][clen][dlen]);
	printf("%d\n", count);
    return 0;
}

