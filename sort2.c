#include <stdio.h>
 
int main(void) {
	   int n, a, i;
    int counts[100000] = {0};
 
    scanf("%d", &n);
    for (i = 0; i < n; i++){
        scanf("%d", &a);
        counts[a]++;
    }
    for (i = 0; i < 100000; i++)
        while (counts[i] > 0){
            printf("%d ", i);
            counts[i]--;
        }
    printf("\n");
 
    return 0;
}
