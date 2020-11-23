/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int *array = (int *)malloc(sizeof(int) * 2);
    array[0] = 0;
    array[1] = 0;
    int a, b;

    for(int i=0; i<numsSize; i++) {
        a = nums[i];
        for(int j=i+1; j<numsSize; j++) {
            b = nums[j];
            if ((a + b) == target) {
                array[0] = i;
                array[1] = j;
                return array;
            }
         }
    }
    return array;
}
