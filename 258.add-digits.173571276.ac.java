/*
 * [258] Add Digits
 *
 * https://leetcode.com/problems/add-digits/description/
 *
 * algorithms
 * Easy (52.53%)
 * Total Accepted:    209.3K
 * Total Submissions: 398.3K
 * Testcase Example:  '38'
 *
 * Given a non-negative integer num, repeatedly add all its digits until the
 * result has only one digit.
 * 
 * Example:
 * 
 * 
 * Input: 38
 * Output: 2 
 * Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
 * Since 2 has only one digit, return it.
 * 
 * 
 * Follow up:
 * Could you do it without any loop/recursion in O(1) runtime?
 * 
 */
class Solution {
    public int addDigits(int num) {
        int sum = 0;
        
        String s = String.valueOf(num);
        for (int i = 0; i < s.length(); i++) {
            sum = sum + (s.charAt(i) - '0');
        }
        
        if (sum < 10) {
            return sum;
        } else {
            return addDigits(sum);
        }
        
    }
}
