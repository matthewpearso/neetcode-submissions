class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums: number[]): number[] {
        let res: number[] = nums.concat(nums);
        return res
    }
}
