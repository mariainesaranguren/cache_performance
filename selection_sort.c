//selection sort

#include <stdio.h>

int arr [1000];
int m_z = 2;
int m_w = 1;
int randInt();

int main() {

//    int arr[1000];

    //generate random numbers
    int i;
    for (i = 0; i < 1000; i++) arr[i] = randInt();
/*
    printf("unsorted numbers:\n");
    for (i = 0; i < 1000; i++)
        printf("%d\n", arr[i]);
*/    

    int back;
    for (back = 1000-1; back > 0; back--) {
        int largest = 0;
        for (i = 1; i <= back; i++) 
            if (arr[i] > arr[largest]) largest = i;
        int temp = arr[largest];
        arr[largest] = arr[back];
        arr[back] = temp;
    }
/*
    printf("sorted numbers:\n");
    for (i = 0; i < 1000; i++)
        printf("%d\n", arr[i]);
*/
    return 0;
}

int randInt() {
  m_z = 36969 * (m_z & 65535) + (m_z >> 16);
  m_w = 18000 * (m_w & 65535) + (m_w >> 16);
  return (m_z << 16) + m_w;
}


// vim: set sts=4 sw=4 ts=8 expandtab ft=cpp:
