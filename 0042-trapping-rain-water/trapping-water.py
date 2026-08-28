class Solution:
    def trap(self, height):
        if not height:
          
            return 0

        left = 0
        right = len(height) - 1
        left_max = 0
      
        right_max = 0
        water_trapped = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                  
                    left_max = height[left]
                else:
                    water_trapped += left_max - height[left]

                left += 1

            else:
                if height[right] >= right_max:
                  
                    right_max = height[right]
                else:
                    water_trapped += right_max - height[right]

                right -= 1

        return water_trapped
