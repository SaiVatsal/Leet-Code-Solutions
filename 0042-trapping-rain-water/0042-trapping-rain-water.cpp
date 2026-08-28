#include <stdio.h>

int trap(int* height, int heightSize) {
    if (heightSize == 0)
        return 0;

    int left = 0;
    
    int right = heightSize - 1;
    
    int left_max = 0;
    
    int right_max = 0;
    
    int water_trapped = 0;
// length of right left max and min trapped water according to image
    while (left < right) {
        
        if (height[left] < height[right]) {

            if (height[left] >= left_max) {
                left_max = height[left];
            } else {
                water_trapped += left_max - height[left];
            }

            left++;
// increament 
        } else {

            if (height[right] >= right_max) {
                right_max = height[right];
            } else {
                water_trapped += right_max - height[right];
            }

            right--;
        }
    }

    return water_trapped;
}
