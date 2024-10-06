
public class queens {

    final int n = 4;

    void printSolution(int board[][], int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 1) {
                    System.out.print("Q ");
                } else {
                    System.out.print(". ");
                }
            }
            System.out.println();
        }
    }

    boolean isSafe(int board[][], int row, int col) {
        int i, j;

        for (i = 0; i < col; i++) {
            if (board[row][i] == 1) {
                return false;
            }
        }

        for (i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 1) {
                return false;
            }
        }

        for (i = row, j = col; j >= 0 && i < n; i++, j--) {
            if (board[i][j] == 1) {
                return false;
            }
        }

        return true;
    }

    boolean solveNQutil(int board[][], int col) {

        if (col == n) {
            return true;
        }

        for (int i = 0; i < n; i++) {
            if (isSafe(board, i, col)) {
                board[i][col] = 1;

                if (solveNQutil(board, col + 1)) {
                    return true;
                }

                board[i][col] = 0;
            }
        }
        return false;
    }

    boolean solveNQ() {
        int board[][] = new int[n][n];
        if (!solveNQutil(board, 0)) {
            System.out.println("Solution does not exist");
            return false;
        }
        printSolution(board, n);
        return true;
    }

    public static void main(String args[]) {
        queens Queen = new queens();
        Queen.solveNQ();
    }
}
