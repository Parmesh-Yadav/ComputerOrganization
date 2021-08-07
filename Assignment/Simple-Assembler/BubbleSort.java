import java.util.Arrays;
import java.util.Scanner;

public class BubbleSort {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n  = s.nextInt();
        int[] l = new int[n];
        for(int i = 0; i < n; i++){
            l[i] = s.nextInt();
        }
        s.close();
        System.out.println("Unsorted array is: " + Arrays.toString(l));
        System.out.println("Sorted array using bubble sort is: " + Arrays.toString(bubbleSort(l)));

    }
    public static int[] bubbleSort(int[] l) {
        int L = l.length;
        for(int i = 0; i<L ; i ++){
            for(int j = 0; j<L-1-i;j++){
                if(l[j] > l[j+1]){
                    int temp = l[j];
                    l[j] = l[j+1];
                    l[j+1] = temp;
                }
            }
        }
        return l;
    }
}
