"""
Single File Programming Question
KMP Algorithm for Pattern Searching



Raj is working on a project that involves searching for a specific pattern in a given text. He has heard about the Knuth-Morris-Pratt (KMP) algorithm, which is efficient for string matching, and he decided to implement it.



Write a program that takes a text and a pattern as input, and then applies the KMP algorithm to find and print all pattern occurrences within the text.

Input format :
The first line of input consists of the text string txt, representing the main string where the pattern needs to be searched.

The second line of input consists of the pattern string pat, that Raj wants to find within the text as a string.

Output format :
If the pattern is found, print "Found pattern at index i", where i is the index of the first occurrence of the pattern in the text.

If the pattern is not found, print "Pattern not found".



Refer to the sample output for the formatting specifications.

Code constraints :
In this scenario, the given test cases will fall under the following constraints:

1 ≤ |txt| ≤ 50

1 ≤ |pat| ≤ 25

The input strings are case-sensitive.

The index starts from 0.

Sample test cases :
# --------------------------------
Input 1 :
ABABDABACDABABCABAB
ABABCABAB
Output 1 :
Found pattern at index 10
# --------------------------------
Input 2 :
ababcababcabcabc
abc
Output 2 :
Found pattern at index 2
Found pattern at index 7
Found pattern at index 10
Found pattern at index 13
Input 3 :
ABC
XY
Output 3 :
Pattern not found
Input 4 :
AABAACAADAABAABA
AABA
Output 4 :
Found pattern at index 0
Found pattern at index 9
Found pattern at index 12
"""

def compute_lps(pat):
    lps = [0] * len(pat)
    length = 0
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
    lps = compute_lps(pat)

    i = 0  # index for txt
    j = 0  # index for pat
    found = False

    while i < n:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == m:
            print(f"Found pattern at index {i - j}")
            found = True
            j = lps[j - 1]
        elif i < n and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    if not found:
        print("Pattern not found")

# Read input
txt = input().strip()
pat = input().strip()

# Search pattern in text
kmp_search(txt, pat)
