/*
 * =====================================================================================
 *
 *       Filename:  prb81.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/09/12 17:30:35
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Sahithi Singam (), sahithi.cse@gmail.com
 *        Company:  
 *
 * =====================================================================================
 */
#include<stdio.h>
#include<stdlib.h>
#define SZ 8
int main()
{
	int mrow = SZ;
	int mcol = SZ;
	int a[SZ][SZ];
	unsigned int sum;// = a[0][0];
	unsigned int r, c;

	unsigned int ch;
	for (r = 0; r < mrow; r++) 
		for (c = 0; c < mcol; c++) {
			scanf("%i", &ch);
			printf("%d ", ch);
			a[r][c] = ch;
		}
		

#if 0
	for (r = 0; r < mrow; r++) {
		for (c = 0; c < mcol; c++) 
			printf("%d ", a[r][c]);
		printf("\n");
	}
#endif
	r = 0, c = 0;
	sum = 0;
	while (((r+1) < mrow) && ((c+1) < mcol)) {
			sum += a[r][c];
			printf("%d %d, a[r][c]= %d, %d\n", r, c, a[r][c], sum);
			if (a[r][c+1] < a[r+1][c])
				c = c + 1;
			else
				r = r + 1;
	}
	printf("r=%d \n c =%d\n, sum = %d", r ,c, sum);
	if (c == (mcol-1)) {
		while (r < mrow) {
			sum += a[r][c];
			r++;
		}
	}
	else {
		while (c < mcol)  {
			sum += a[r][c];
			c++;
		}
		
	}

	printf("sum = %d\n", sum);
		

}
