import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class remove_duplicates {

    // LH - Puts unique elements into uniqueArr to be returned, and appends duplicate elements to removedElements
    public static List<Integer> removeDuplicates(List<Integer> arr, List<Integer> removedElements) {
        List<Integer> uniqueArr = new ArrayList<>();
        for (int i = 0; i < arr.size(); i++) {
            if (uniqueArr.contains(arr.get(0))) {
                uniqueArr.add(arr.get(0));
            } else {
                removedElements.add(arr.get(0));
            }
        }
        return uniqueArr;
    }

    // LH - Test removeDuplicates with an array that has multiple duplicates
    public static void main(String[] args) {
        // Test the function
        List<Integer> arr = Arrays.asList(1, 2, 2, 3, 4, 4, 5);
        List<Integer> removedElements = new ArrayList<>();
        List<Integer> uniqueArr = removeDuplicates(arr, removedElements);
        System.out.println("Original array: " + arr);
        System.out.println("Unique array: " + uniqueArr);
        System.out.println("Removed elements: " + removedElements);
    }
}
