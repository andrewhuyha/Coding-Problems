class Solution {
    public int[] twoSum(int[] nums, int target) {
        //O(n) time complexity
        //Iterate through the array, if the element exists in the map, check for it's complement, then return the index of the positions.
        
        //Initialize empty HashMap
        HashMap<Integer, Integer> map = new HashMap<>();
        
        //Iterate over the elements in the array
        for(int i = 0; i < nums.length; i++){
            int complement = target - nums[i];
        //If the complement exists, return the array
            if(map.containsKey(complement)){
                return new int[]{
                    map.get(complement), i
                };
            }else{
                map.put(nums[i], i);
            }
        }
        return new int[]{};
        
    }
}
