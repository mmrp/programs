#include <stdio.h>
long long power_mod(long long a, int p, int m)
{   
	if (p == 1 || p == 0)
		return a%m;
	long long c = a*a;
	if (c > m)
		a = c%m;

	if (p%2 == 0)
		return power_mod(a, p/2, m)%m;

	return (a*power_mod(a, (p-1)/2, m))%m;
}


int main(int argc, char *argv[])
{
	long long a;
	int p;
	int m;
	a = atoi(argv[1]);
	p = atoi(argv[2]);
	m = atoi(argv[3]);
	printf("%lld\n", power_mod(a, p, m));

}

