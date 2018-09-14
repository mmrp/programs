#include <stdio.h>
long long modinv(long long u, long long v)
{
    long long inv, u1, u3, v1, v3, t1, t3, q;
    int iter;
    /* Step X1. Initialise */
    u1 = 1;
    u3 = u;
    v1 = 0;
    v3 = v;
    /* Remember odd/even iterations */
    iter = 1;
    /* Step X2. Loop while v3 != 0 */
    while (v3 != 0)
    {
        /* Step X3. Divide and "Subtract" */
        q = u3 / v3;
        t3 = u3 % v3;
        t1 = u1 + q * v1;
        /* Swap */
        u1 = v1; v1 = t1; u3 = v3; v3 = t3;
        iter = -iter;
    }
    /* Make sure u3 = gcd(u,v) == 1 */
    if (u3 != 1)
        return 0;   /* Error: No inverse exists */
    /* Ensure a positive result */
    if (iter < 0)
        inv = v - u1;
    else
        inv = u1;
    return inv;
}

long long power_mod(long long a, long long p, long long mod)
{
	long long c = 1;
	while (p) {
		if (p & 1)
			c = (c * a) % mod;
		a = (a * a) % mod;
	}
	return c;
}

long long CRT(long long a1, long long m1, long long a2, long long m2)
{
	long long M;
	M = m1 * m2;
	return ((a1 * modinv(m1, m2)) + (a2 * modinv(m2, m1))) % M;
}

long long FLT(long long a, long long p, long long mod)
{


}

int arr[5][4];
long long power_tower(long long a, long long p, long long m1, long long m2)
{
	if (p == 2) 
		return power_mod(a, a, (m1 * m2));

	power_tower(a, p%Q(m1)

	

}

int main()
{
    int m, n;
	arr[2][0] = 1; 
	arr[2][1] = 2;
	arr[2][2] = 4;
	arr[2][3] = 16;
	arr[2][4] = 65536;
	arr[2][5] = 719156736;
	arr[3][0] = 1;
	arr[3][1] = 3;
	arr[3][2] = 27;
	arr[3][3] = 597484987; 
	arr[4][0] = 1; 
	arr[4][1] = 4; 
	arr[4][2] = 16; 
    scanf("%d %d", &m, &n);
    printf("%d\n", modinv(m, n));
}
