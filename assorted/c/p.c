#include <stdio.h>

long long arr[10000+10];
int find_sol(long long  arr[], int n, long long v)
{
	int i;

	for (i = 0; i < n; i++)
		if (v % arr[i] == 0)
            return 1;

    return 0;
}

long long get_total_jobs(long long  arr[], int n, long long v)
{
	int i;
	long long sum = 0;

	for (i = 0; i < n; i++)
		sum += v/arr[i];

	return sum;
}

long long get_time(long long arr[], int n, int min, long long T)
{
	long long low, mid, high;
	long long tjobs;
	
	low  = 0;
	high = min * T;
	mid  = (low+high)/2;
	while (1) {
//print low, mid, high
		tjobs = get_total_jobs(arr, n, mid);
//		printf("%lld %lld %lld: %lld, %lld\n", low, mid, high, tjobs, T);
//print tjobs
		if (tjobs >= T)
			if (get_total_jobs(arr, n, mid-1) < T)
				break;

		if (tjobs < T)
			low = mid+1;
		else
			high = mid-1;
		 
		mid = (low+high)/2;
	}
	return (mid);
}

int main()
{
	int t;
	int n;
	long long T;
	int i;
	int min = 1000000001;
	scanf("%d", &t);
	while (t--) {
		scanf("%d %d", &n, &T);
		for (i = 0; i < n; i++) {
			scanf("%lld", &arr[i]);
			if (min > arr[i])
				min = arr[i];
		}
		if (n == 1) 
			printf("%lld\n", arr[0] * T);
		else
			printf("%lld\n", get_time(arr, n, min, T));
	}
				
	return 0;
}
