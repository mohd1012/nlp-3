import java.util.Scanner;
/**
 * This computes the minimum edit distance and gives feedback about the edits of two strings.
 * It is a very basic algorithm using Levenshtein's method of equating substitution of characters
 * to 2 edits and insertion or deletion of a character to be 1 edit.
 * 
 * @author Andie Rocca
 * @version 1.0
 */
public class EditDistance
{
    private String x;
    private String y;

    /**
     * Constructor for EditDistance
     * @param x first String
     * @param y second String
     */
    public EditDistance(String x, String y)
    {
        this.x = "-" + x;
        this.y = "-" + y;
    }

    public int computeDistance() {
        int[][] table = new int[x.length()][y.length()];
        //fill table with initial values
        for (int i = 0; i < table.length; i++) {
            table[i][0] = i;
        }
        for (int i = 0; i < table[0].length; i++) {
            table[0][i] = i;
        }
        
        int minDistance; //min distance between insertion, deletion, and substitution
        int sub; //will be a 0 or a 2 based on whether the characters are the same
        for (int i = 1; i < x.length(); i++) {
            for (int j = 1; j < y.length(); j++) {
                sub = (x.charAt(i) == y.charAt(j)) ? 0 : 2;
                minDistance = Math.min(table[i-1][j-1] + sub, 
                    Math.min(table[i-1][j] + 1, table[i][j-1] + 1));
                table[i][j] = minDistance;
            }
        }
        
        return table[table.length - 1][table[0].length - 1];
    }

    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        System.out.println("First string: ");
        String a = input.nextLine();
        System.out.println("Second string: ");
        String b = input.nextLine();

        EditDistance minED = new EditDistance(a, b);
        System.out.println("Minimum number of edits: " + minED.computeDistance());
    }
}
