//Bubble Sort Algorithm
	//Best Case Performace: O(n) time | O(1) space
	//Worst Case Performace: O(n^2) time | O(1) space
import java.util.*;
class Program {
	//Checks in case of empty array
  public static int[] bubbleSort(int[] array) {
		if(array.length == 0){
			return new int[] {};
		}
    // Write your code here.
		//For loop for passes through array
		for(int i = 0; i < array.length; i++){
			//For loop that keeps track of individual position
			for(int j = 0; j < array.length-1; j++){
				//Swap
				if(array[j] > array[j+1]){
					int temp = array[j];
					array[j] = array[j+1];
					array[j+1] = temp;
				}
			}
		}
		return array;
  }
}
