#include <stdio.h>

int arr[100+1];
void get_base(int num, int base)
{
	int p, i;
	p = 100;
	while (num) {
		printf("%d\n", num%base);
		arr[p--] = num % base;
		num /= base;
		printf("%d\n", num);
	}
	if (num) 
		arr[p] = num;
	else
		p++;

	for (i = p; i<= 100; i++)
		printf("%d ", arr[i]);
	printf("\n");
}


int main()
{
	int base;
	int num;
	scanf("%d %d", &num, &base);
	get_base(num, base);
}
