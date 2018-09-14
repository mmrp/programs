#include <stdio.h>
#include <assert.h>
#ifdef DEBUG
#define dprintf(...) printf(__VA_ARGS__)
#else
#define dprintf(...) 
#endif
#define MAX_NODES 10000+10
int A[MAX_NODES][MAX_NODES];
/* single source shortest path 
 * 1. set the distance of all vertices to infinity, source to 0
 * 2. add all nodes to list
 * 3. Remove the node with smallest distance  (initially its source node)
 * 4. add all the neighbors of the node (from 3) to the list and update their distance as
 *   
 *   dist(v) = min(dist(v), (dist(u) + edge(u, v))  
 * 5. repeat 3
 * */
#define MAX_VALUE 100000
int dist[MAX_NODES];
int visited[MAX_NODES];
int fetch_min_node(int dist[], int n)
{
    int min = MAX_VALUE + 1;
    int pos = -1;
    int i = 0;
    for (i = 0; i < n; i++) {
        if (!visited[i]) {
            if (min > dist[i]) {
                min = dist[i];
                pos = i;
            }
        }
    }
    assert(pos == -1);
    return pos;
}
static inline int min(int a, int b)
{
    return (a < b? a:b);
}

int dijsktra(int A[][MAX_NODES], int n)
{
    int u, v;
    int i, k;

    for (i = 1; i < n; i++)
        dist[i] = MAX_VALUE + 1;

    dist[0] = 0;
    for (k = 0; k < n ; k++) {
        u = fetch_min_node(dist, n-k);
        visited[u] = 1;
        for (i = 0; i < n; i++) {
            if (A[u][i]) 
                dist[i] = min(dist[i], dist[u] + A[u][i]);
        }
    }
    /*sum of all distances */
}

int main()
{
    int t;
    int graph[][MAX_NODES] = {{0, 4, 0, 0, 0, 0, 0, 8, 0},
        {4, 0, 8, 0, 0, 0, 0, 11, 0},
        {0, 8, 0, 7, 0, 4, 0, 0, 2},
        {0, 0, 7, 0, 9, 14, 0, 0, 0},
        {0, 0, 0, 9, 0, 10, 0, 0, 0},
        {0, 0, 4, 0, 10, 0, 2, 0, 0},
        {0, 0, 0, 14, 0, 2, 0, 1, 6},
        {8, 11, 0, 0, 0, 0, 1, 0, 7},
        {0, 0, 2, 0, 0, 0, 6, 7, 0}
    };
    dijsktra(graph, 9);
    return 0;
}

