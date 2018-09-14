#include <stdio.h>
#include <string.h>


#ifdef DEBUG
#define dprintf(fmt, ...) do { fprintf(stderr, fmt, __VA_ARGS__); } while (0)
#else
#define dprintf(fmt, ...) 
#endif
#define MAX_STRING 100000
#define modulus 1000000007
char S[MAX_STRING];
long long  D[MAX_STRING];
int  last[26];

int main()
{
    int t;
	int i, len;
	int lpos;
    scanf("%d", &t);
    while (t--){
		scanf("%s", &S[1]);
		len = strlen(&S[1]);
		D[0] = 1;
		for (i = 1; i <= len; i++) {
			D[i] = D[i-1] * 2;
			lpos = S[i]-'A';
			if (last[lpos])
				D[i] = D[i] - D[last[lpos] - 1];
			D[i] = (D[i] + modulus)% modulus;
			last[lpos] = i;
			dprintf("d[%d] : %d\n", i, D[i]);
		}
		printf("%lld\n", D[len]);
		memset(D, 0, sizeof(D));
		memset(last, 0, sizeof(last));
    }
    return 0;
}

