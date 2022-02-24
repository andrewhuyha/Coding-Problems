class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<Integer>();
        //Iterate through input
        for(int i: nums){
            //If we see that the set has seen the value already, we will return true
            if(set.contains(i)){
                return true;
            //Otherwise, we will add it to the set
            }else{
                set.add(i);
            }
        }
        return false;
    }
}
