//Merge Sort Algorithm
//O(nlog(n)) Time | O(n(log(n))) Space

import java.util.*;

class Program {
  public static int[] mergeSort(int[] array) {
		//Base Case: Checks if array is empty or contains only one value
		if(array.length <= 1){
			return array;
		}
		
		int middleIndex = array.length / 2;
		//Arrays.copyOfRange copies [orignial array, start point, end point]
		int[] leftHalf = Arrays.copyOfRange(array, 0, middleIndex);
		int[] rightHalf = Arrays.copyOfRange(array, middleIndex, array.length);
		return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf));
  }
	
public static int [] mergeSortedArrays(int[] leftHalf, int[] rightHalf){
	//Creates a sorted array with length of the added two halves
	int[] sortedArray = new int[leftHalf.length + rightHalf.length];
	//k is the pointer of the current index
	int k = 0;
	//i is the pointer of the left half
	int i = 0;
	//j is the pointer of the right half
	int j = 0;
	
	//Continues to check if there are still numbers in the left and right halves
	while(i < leftHalf.length && j < rightHalf.length){
		//If the number in the left half is less than number in right, add it to the sorted array then move index
		if(leftHalf[i] <= rightHalf[j]){
			sortedArray[k++] = leftHalf[i++];
		}
		//Otherwise the right half number moves into the sorted array
		else{
			sortedArray[k++] = rightHalf[j++];
		}
	}
	//While there are still numbers in the half, add them into the sorted array.
	while(i < leftHalf.length){
		sortedArray[k++] = leftHalf[i++];
	}
	while(j < rightHalf.length){
		sortedArray[k++] = rightHalf[j++];
	}
	return sortedArray;
}
}
