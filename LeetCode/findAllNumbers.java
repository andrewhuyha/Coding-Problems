class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        //Create the output array
        List<Integer> missingNumbers = new ArrayList<Integer>();
        
        //Create HashSet to check to see which numbers are seen in nums
        HashSet<Integer> numbers = new HashSet<Integer>();
        for(int i: nums){
            numbers.add(i);
        }
        //Loop through nums, if the number isn't in the HashSet, we will add it to our arrayList
        for(int i = 1; i <= nums.length; i++){
            if(!numbers.contains(i)){
                missingNumbers.add(i);
            }
        }
        return missingNumbers;
    }
}
