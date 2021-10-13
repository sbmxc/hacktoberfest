#include <stdio.h>

/* Calculate mean of N elements
 * @begin: a pointer to first element of an array
 * @end: a ponter to last element of an array
*/
float mean(float* begin, float* end) {
    float sum = 0;
    int n = end - begin;
    while(begin != end)
    {
        sum += *(begin++);
    }
        
    return sum / n;
}

int main() {
    float values[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    printf("mean: %f\n", mean(values, values+10));
    return 0;
}