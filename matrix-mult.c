#include "mipslib.h"
#define N 36

//int A[N][N] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
//int B[N][N] = {{7, 1, 4, 6}, {3, 2, 5, 1}, {6, 1, 8, 2}, {4, 8, 7, 9}};
//int C[N][N];

int A[N][N];
int B[N][N];
int C[N][N];

int main()
{
    int i, j, k;
    for (i = 0;  i < N;  i++)
        for (j = 0;  j < N;  j++)
            C[i][j] = 0;

    for (i = 0;  i < N;  i++)
        for (j = 0;  j < N;  j++)
            for (k = 0;  k < N;  k++)
                C[i][j] += A[i][k] * B[k][j];

//    for (i = 0;  i < N;  i++) {
//        for (j = 0;  j < N;  j++) {
//            printf("%d\t", C[i][j]);
//        }
//        printf("\n");
//    }
}
