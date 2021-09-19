import java.util.*;

class Program {
  public static boolean isPalindrome(String str) {
    //O(n^2) time | O(n) space
		//In this approach we reverse the string and compare it to the original to see if they are equal.
		String reverseString = "";
		//Builds the reverse string
		for(int i = str.length() - 1; i >= 0;  i--){
				reverseString += str.charAt(i);
		}
		if(str.equals(reverseString)){
			return true;
		}
		else{
    return false;
		}
  }
}
