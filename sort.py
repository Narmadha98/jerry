#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int n, a, i;
    int counts[1000] = {0};

    scanf("%d", &n);
    for (i = 0; i < n; i++){
        scanf("%d", &a);
        counts[a]++;
    }
    for (i = 0; i < 1000; i++)
        while (counts[i] > 0){
            printf("%d ", i);
            counts[i]--;
        }
    printf("\n");
    
    return 0;
}

