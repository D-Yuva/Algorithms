"""
Single File Programming Question
Problem Statement



Jansi is a computer science student who loves solving algorithmic problems. Recently, her professor assigned her the task of implementing the Knuth-Morris-Pratt (KMP) string-matching algorithm.



As part of the assignment, she needs to develop a program that takes a text and a pattern as input and outputs the starting and ending indices of all occurrences of the pattern in the text.

Input format :
The first line contains a string txt, representing the text in which Jansi needs to search for occurrences of the pattern.

The second line contains a string pat, representing the pattern that Jansi wants to find in the text.

Output format :
The output should print the starting and ending positions of all occurrences of the pattern within the text.



For each occurrence of the pattern in the text, print two space-separated integers on a new line. These integers represent the starting and ending indices (1-indexed) of the substring in the text that matches the pattern.



If the pattern is not found, nothing will be printed.



Refer to the sample output for the formatting specifications.

Code constraints :
1 <= |txt| <= 50

1 <= |pat| <= 25

The input strings should be case-sensitive.

The index starts from 1.

Sample test cases :
# --------------------------------
Input 1 :
ABABDABACDABABCABAB
ABABCABAB
Output 1 :
11 19
# --------------------------------
Input 2 :
Pen,pencil,Penguin
Pen
Output 2 :
1 3
12 14
"""

def compute_lps_array(pat):
    lps = [0] * len(pat)
    length = 0  # length of the previous longest prefix suffix
    i = 1

    while i < len(pat):
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(txt, pat):
    n = len(txt)
    m = len(pat)
    lps = compute_lps_array(pat)
    i = 0  # index for txt[]
    j = 0  # index for pat[]

    while i < n:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == m:
            # Match found at index (i - j), convert to 1-indexed output
            print(f"{i - j + 1} {i}")
            j = lps[j - 1]  # Continue checking for next matches
        elif i < n and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

# Read input
txt = input().strip()
pat = input().strip()

# Perform pattern search
kmp_search(txt, pat)
