"""A palindromic number reads the same both ways. The smallest 6 digit
palindrome made from the product of two 3-digit numbers is 101101=143×707.

Find the largest palindrome made from the product of two 3-digit numbers which
is less than N.

Input Format
First line contains T that denotes the number of test cases. This is followed
by T lines, each containing an integer, N.

Output Format
Print the required answer for each test case in a new line.

Constraints
1≤T≤100
101101<N<1000000
Sample Input

2
101110
800000
Sample Output

101101
793397
"""


for _ in xrange(int(raw_input())):
    n = int(raw_input())
    print (n**3 - n) * (3 * n + 2) / 12
