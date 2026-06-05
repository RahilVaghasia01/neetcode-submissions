class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> knowen_ele = new HashSet<>();
        for(int i : nums) {
            if(knowen_ele.contains(i)) {
                return true;
            }
            else {
                knowen_ele.add(i);
            }
        }
        return false;
    }
}