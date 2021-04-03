class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)==2:
            return min(height[0], height[1])
        
        left = 0
        right =len(height)-1
        max_area = 0
        
        while left < right:
            temp_width = right - left
            temp_height = min(height[left], height[right])
            area = temp_width*temp_height
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            max_area = max(area, max_area)
        return max_area