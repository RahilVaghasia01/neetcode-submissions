class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seen = new HashMap<>();
        int len = nums.length;
        for(int i = 0; i < len; i++){
            int ele = target - nums[i];
            if(seen.containsKey(ele)) {
                return new int[] {seen.get(ele), i};
            }
            seen.put(nums[i], i);
        }
        return new int[] {};
    }
}
