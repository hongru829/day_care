/*
 * [289] Game of Life
 *
 * https://leetcode.com/problems/game-of-life/description/
 *
 * algorithms
 * Medium (39.59%)
 * Total Accepted:    81K
 * Total Submissions: 204.5K
 * Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
 *
 * According to the Wikipedia's article: "The Game of Life, also known simply
 * as Life, is a cellular automaton devised by the British mathematician John
 * Horton Conway in 1970."
 * 
 * Given a board with m by n cells, each cell has an initial state live (1) or
 * dead (0). Each cell interacts with its eight neighbors (horizontal,
 * vertical, diagonal) using the following four rules (taken from the above
 * Wikipedia article):
 * 
 * 
 * Any live cell with fewer than two live neighbors dies, as if caused by
 * under-population.
 * Any live cell with two or three live neighbors lives on to the next
 * generation.
 * Any live cell with more than three live neighbors dies, as if by
 * over-population..
 * Any dead cell with exactly three live neighbors becomes a live cell, as if
 * by reproduction.
 * 
 * 
 * Write a function to compute the next state (after one update) of the board
 * given its current state. The next state is created by applying the above
 * rules simultaneously to every cell in the current state, where births and
 * deaths occur simultaneously.
 * 
 * Example:
 * 
 * 
 * Input: 
 * [
 * [0,1,0],
 * [0,0,1],
 * [1,1,1],
 * [0,0,0]
 * ]
 * Output: 
 * [
 * [0,0,0],
 * [1,0,1],
 * [0,1,1],
 * [0,1,0]
 * ]
 * 
 * 
 * Follow up:
 * 
 * 
 * Could you solve it in-place? Remember that the board needs to be updated at
 * the same time: You cannot update some cells first and then use their updated
 * values to update other cells.
 * In this question, we represent the board using a 2D array. In principle, the
 * board is infinite, which would cause problems when the active area
 * encroaches the border of the array. How would you address these problems?
 * 
 * 
 */
public class Solution {
    public void gameOfLife(int[][] board) {
        
        if(board==null||board[0].length==0) return;
        
        int m = board.length;
        int n = board[0].length;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                int lives = helper(board,i,j);
                //System.out.println(lives);
                if(board[i][j]==1){
                    if(lives<2){
                        board[i][j] = 2;
                    }
                    else if(lives>3){
                        board[i][j] = 2;
                    }
                }
                else{
                    if(lives==3){
                        board[i][j] = 3;
                    }
                }
            }
        }
        
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                board[i][j] = board[i][j]%2;
            }
        }
        return;
        
    }
    
    public int helper(int[][] board,int x,int y){
        
        int m = board.length;
        int n = board[0].length;
        
        int[] dx = {-1,-1,-1,0,0,1,1,1};
        int[] dy = {-1,0,1,-1,1,-1,0,1};
        
        int newX = 0;
        int newY = 0;
      
        int count = 0;
        for(int i=0;i<8;i++){
            newX = x+dx[i];
            newY = y+dy[i];
            
            if(newX<0||newY<0||newX>=m||newY>=n){
               // System.out.println(newX+" "+newY);
                continue;
            }
            if(board[newX][newY]>0&&board[newX][newY]<3){
                count++;
            }
        }
    
        return count;
    }
}
