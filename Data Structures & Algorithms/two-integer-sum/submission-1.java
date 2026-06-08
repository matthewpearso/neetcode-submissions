class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] empty = {};
        if(nums.length < 1){
            return empty;
        }
        
        Map<Integer, Integer> myMap = new HashMap<>();
        
        for(int i = 0; i < nums.length; i++){
            int complement = target - nums[i];
            if(myMap.containsKey(complement)){
                int j = myMap.get(complement);
                int[] results = {j, i};
                return results;
            }
            else{
                myMap.put(nums[i], i);
            }
        }
        return empty;
    }
}
