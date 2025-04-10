"""
Single File Programming Question
Problem Statement



Given two strings, text1, and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.



A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde".



A common subsequence of two strings is a subsequence that is common to both strings.

Input format :
The first line of input consists of a string representing text1.

The second line of input consists of a string representing text2.

Output format :
The output prints a single integer which is the length of the Longest Common Subsequence of the two strings.



Refer to the sample output for the formatting specifications.

Code constraints :
In the given scenario, the test cases will fall under the following constraints:

1 ≤ text1.length, text2.length ≤ 100

text1 and text2 consist of only lowercase English characters.
"""

# --------------------------------
# INPUT
# abcde
# ace
# -----
# OUTPUT
# 3
# --------------------------------

def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    
    # Create a 2D dp array of size (m+1) x (n+1) initialized to 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]  # match found
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # take max of left or top

    return dp[m][n]

# Input reading
text1 = input().strip()
text2 = input().strip()

# Output the result
print(longest_common_subsequence(text1, text2))


