class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        l = 0
        r = l
        cache = {nums[l]:1}
        
        while r < len(nums) - 1:
            
            if r - l < k:
                r += 1
                cache[nums[r]] = cache.get(nums[r], 0) + 1
                if cache[nums[r]] > 1:
                    return True
            else:
                cache[nums[l]] -= 1
                l += 1
        
        return False



        