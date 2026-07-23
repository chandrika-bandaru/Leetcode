int uniqueXorTriplets(int* nums, int numsSize) {
    if (numsSize == 1) return 1;
    if (numsSize == 2) return 2;
    
    int msb = 0;
    while ((1 << (msb + 1)) <= numsSize) {
        msb++;
    }
    
    return 1 << (msb + 1);
}