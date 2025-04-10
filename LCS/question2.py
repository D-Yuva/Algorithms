"""
Single File Programming Question
Problem Statement



﻿Emma, a software developer, is working on a plagiarism detection tool for an educational platform. The platform receives large text documents from students, and Emma needs to compare the submitted papers to check for similarities. She decides to implement an algorithm that finds the Longest Common Subsequence (LCS) between two documents, which are represented as strings. To achieve this, Emma needs a program that can efficiently calculate the length of the LCS for these large document strings.



Help Emma by writing a program that calculates the length of the LCS between two given document strings

Input format :
The first line of input contains a string representing the first document.

The second line of input contains a string representing the second document.

Output format :
The first line of output displays all the unique combinations of the longest common subsequence.

The last line of output displays the length(counted based on the number of characters in the subsequence including the spaces between words) of the longest common subsequence.



Refer to the sample output for the formatting specifications.

Code constraints :
In the given scenario, the test cases fall under the following constraints:

0 ≤ len(str1), len(str2) ≤ 1000
"""
"""
# --------------------------------
Sample test cases :
Input 1 :
This is test
is test This
# -----
Output 1 :
is test
The length of the Longest Common Subsequence is: 7
# --------------------------------
Input 2 :
The brown quick fox
The quick brown fox
# -----
Output 2 :
The brown fox
The quick fox
The length of the Longest Common Subsequence is: 13
"""

def lcs(word1, word2):
    m = len(word1)
    n = len(word2)

    dp = [[[] for _ in range(n+1)]for _ in range (m+1)]

    for i in range(m):
        for j in range(n):
            if (word1[i] == word2[j]):
                for seq in dp[i][j]:
                    dp[i+1][j+1].append(seq + [word1[i]])
                if not dp[i][j]:
                        dp[i+1][j+1].append([word1[i]])
            else: 
                len_up = len(" ".join(dp[i][j+1][0])) if dp[i][j+1] else 0
                len_left = len(" ".join(dp[i+1][j][0])) if dp[i+1][j] else 0
                
                if len_up > len_left:
                    dp[i+1][j+1] = dp[i][j+1].copy()
                elif len_up < len_left:
                    dp[i+1][j+1] = dp[i+1][j].copy()
                else:
                    seqs = dp[i][j+1] + dp[i+1][j]

                    seen = set()
                    unique = []

                    for s in seqs:
                        t = tuple(s)
                        if t not in seen:
                            seen.add(t)
                            unique.append(s)
                    
                    dp[i+1][j+1] = unique
    
    return dp[m][n]

str1 = input().strip()
str2 = input().strip()

word1 = str1.split()
word2 = str2.split()

sequences = lcs(word1, word2)

unqiue_lcs = set(" ".join(seq) for seq in sequences)

for seq in sorted(unqiue_lcs):
    print(seq)

if unqiue_lcs:
    length = len(list(unqiue_lcs)[0])
else:
    length = 0

print(length)