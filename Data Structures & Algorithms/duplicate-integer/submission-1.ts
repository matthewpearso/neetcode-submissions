class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const track = new Set<number>();
        for(let i = 0; i < nums.length; i++){
            if (track.has(nums[i])){
                return true
            }
            track.add(nums[i])
        }
        return false
    }
}
