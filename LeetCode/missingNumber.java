class Solution {
    public int missingNumber(int[] nums) {
        int solution = 0;
        HashSet<Integer> set = new HashSet<Integer>();
        for(int i: nums){
            set.add(i);
        }
        for(int i = 0; i <= nums.length; i++){
            if(!set.contains(i)){
                solution = i;
            }
        }
        return solution;
    }
}
