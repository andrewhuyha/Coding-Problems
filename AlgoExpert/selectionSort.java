import java.util.*;

class Program {
	//Worst: O(n^2) | O(1) space
  public static int[] selectionSort(int[] array) {
    
		//Returns empty array if input array is null
		if(array.length == 0){
			return new int[] {};
		}
		for(int i = 0; i < array.length-1; i++){
			//Marker at the front of the array
			int index = i;
			for(int j = i + 1; j < array.length; j++){
				if(array[j] < array[index]){
					//Marker advances
					index = j;
				}
			}
      //Swap
			int temp = array[index];
			array[index] = array[i];
			array[i] = temp;
			
		}
		return array;

  }
}
