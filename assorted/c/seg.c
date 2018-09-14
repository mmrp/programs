#include <stdio.h>

#ifdef DEBUG
#define dprintf(fmt, ...) do { fprintf(stderr, fmt, __VA_ARGS__); } while (0)
#else
#define dprintf(fmt, ...) 
#endif
#define MAX_ELEM 100
#define MAX_LEN (2*MAX_ELEM+1)


int M[MAX_LEN];
int A[MAX_ELEM];
int P[MAX_ELEM];
/* M = main tree, n = node of the main tree
 * A = array, range of the array controlled by node n*/
int build_tree(int M[], int n, int A[], int s, int e)
{
	if (s == e) {
		M[n] = A[s];
		P[s] = n;
	}
	else {

		int c1, c2;
		int m;

		m = (s+e)/2;
		c1 = build_tree(M, 2*n, A, s, m);
		c2 = build_tree(M, 2*n+1, A, m+1, e);
		if (c1 < c2) 
			M[n] = c1;
		else
			M[n] = c2;
	}
	printf("[%d - %d] = %d\n", s, e, A[n]);
	return M[n];
}
/* M = tree, n = starting node 
  [p, q] => range to search for 
				
				[0		,			  8, 1]
				/						 \
			[0, 4, 1]					[5,  8,  4]
			/		\					/		  \
		[0,2,1]		[3,4,2]		   [5,6,4]		  [7,8,5]
		 /	 \		/	  \			/	 \		  /		\
	[0,1,1][2,2,6][3,3,7][4,4,2] [5,5,4][6,6,8][7,7,9][8,8,5]
	/	\
[0,0,1] [1,1,3]

say: 1, 3, 6, 7, 2, 4, 8, 9,5

  We are going to tranverse as in build_tree, but will never change p and q
  so, if we are in interval say [l,m] and p <= [l,m] <= q, that means we can
  fetch that interval value.
 
  Lets search for 2, 7: first left subtree
				      [0, 8, 2,7]  
				        /
			         [0,4,2,7] (r=1, R)
		             /		   \
(i)->		   [0,2,2,7](6) [2,4,2,7] [2,7 encompasses the interval, result value] (r=1)
	               /	  \
(ii)->[0,1,2,7](r=-1) [2,2,2,7](r=6)
			(outside)

		[0,8,2,7] (right expansion) 
				\
				 [5,8,2,7] (r=4,L)
				 /		  \
    (iii)->	[5,6,2,7](r=4) [7,8,2,7](r=9,L)
                           /       \
    (iv)->      [7,7,2,7][r=9] [8,8,2,7](r=-1, outside)

	  -------------------------------
		        [0,8,2,7]
		 /                  \
	[0,4,2,7] (a) - 1	 [5,8,2,7] (b) - 4
	result = 1 left tree
*/
int query_tree(int M[], int n, int s, int e, int p, int q)
{
	/* scenerio (i) left subtree
	 * scenrio (iv) right subtree
	 * eg: s <= e < p <= q
	 *     p <= q < s <=e 
	 */
	if (p > e  || q < s) 
		return -1;
	
	/* if p and q encompass the range of s, e
	 * i.e p <= s <= e <= q, return node 
	 * scenerio (i) right subtree
	 * scenrio (iv) left subtree
	 */
	if (p <= s && e <= q)
		return M[n];

	int v1, v2, m;
	m = (s+e)/2;
	v1 = query_tree(M, 2*n, s, m, p, q); 
	v2 = query_tree(M, 2*n+1, m+1, e, p, q); 
	if (v1 == -1)
		return v2;
	if (v2 == -1)
		return v1;
	return (v1 < v2? v1:v2);
}
/* Update a node and propagate up the tree */
int update_tree(int M[], int n, int v, int s, int e)
{
	int p, b, m;
	int l;
#if 0
	/*first find where node n is in the tree */
	l = 1;
	while (s != e) {
		m = (s+e)/2;
		dprintf("%d %d %d\n", l, s, e);
		if (m >= n) { /*goto left subtree*/
			e = m;
			l = 2*l;
		}
		else 
		if (m < n) { /*goto right subtree*/
			s = m+1;
			l = 2*l+1;
		}
	}
	dprintf("%d\n", l);
#else
	l = P[n];
#endif
	n = l;
	M[n] = v; 
	while (n) {
		p = n/2;
		b = 2*p;
		if (n%2 == 0)
			b += 1;
		M[p] = (M[b] < M[n] ? M[b]: M[n]);
		n = n/2;
	}
}

void print_tree(int M[], int N)
{
	int i;
	for (i = 1; i <= 2*N+1; i++)
		printf("%d ", M[i]);
	printf("\n");
	for (i = 1; i <= N; i++)
		printf("%d ", P[i-1]);
	printf("\n");
	
}
int main()
{
	int t, N, i;
	scanf("%d", &N);
	for (i = 0; i < N; i++)
		scanf("%d", &A[i]);

	build_tree(M, 1, A, 0, N-1);
	print_tree(M, N);

	scanf("%d", &t);
	int n, v;
	while (t--) {
		scanf("%d %d", &n, &v); 
		update_tree(M, n, v, 0, N-1);
		print_tree(M, N);
	}
	
	printf("Query: \n");
	int p, q;
	scanf("%d", &t);
	while (t--) {
		scanf("%d %d:", &p, &q);
		printf("%d\n", query_tree(M, 1, 0, N-1, p, q));
	}
	return 0;
}

