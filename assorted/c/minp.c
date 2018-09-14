#include <stdio.h>
#include <string.h>
#ifdef DEBUG
#define dprintf(...) printf(__VA_ARGS__)
#else
#define dprintf(...) 
#endif

#define NMAX 1024
char a[NMAX], b[NMAX];

int d[NMAX+1][NMAX+1];

int min(int a, int b)
{
    return (a <= b? a: b);
}

int palin(char *s, int l, int h)
{
    int a;
    if (l > h)
        return 0;

    if (s[l] == s[h]) 
        a = palin(s, l+1, h-1);
    else
        a = 1 + min(palin(s, l+1, h), palin(s, l, h-1));
    dprintf("%d ", a);
    d[l][h] = a;
    return a;
}

int edit_distance(char *s, char *t, int slen, int tlen)
{
    dprintf("%d, %d\n", slen, tlen);
    int i, j;
    for (i = 0; i <= slen; i++) 
        d[i][0] = 0;

    for (j = 0; j <= tlen; j++) 
        d[0][j] = 0;

    for (j = 1; j <= tlen; j++) {
        for (i = 1; i <= slen; i++) {
            if (s[i] == t[j]) 
                d[i][j] = d[i-1][j-1];
            else 
                d[i][j] =  1 + min(d[i-1][j], d[i][j-1]); 
            dprintf("%d ", d[i][j]);
        }
        dprintf("\n");
    }
    return d[slen][tlen];
}

int main()
{
    int t;
//    scanf("%s %s", &a[1], &b[1]);
//    printf("%d\n", edit_distance(a, b, strlen(&a[1]), strlen(&b[1])));
    scanf("%s", a);
    printf("%d\n", palin(a, 0, strlen(a)-1));
    int i, j, l;
    l = strlen(a);
    printf("  ");
    for (i = 0; i < l; i++) 
        printf("%c ", a[i]);
    printf("\n");
    for (i = 0; i < l; i++) {
        printf("%c ", a[i]);
        for (j = 0;j < l; j++) 
            printf("%d ", d[i][j]);
        printf("\n");
    }
    return 0;
}

