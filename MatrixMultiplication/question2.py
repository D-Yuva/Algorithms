"""
Single File Programming Question
Problem Statement



Emily is managing a factory that operates on sequential machines represented by matrices. Each machine outputs data in a format that matches the input dimensions of the next machine. To reduce processing time, Emily wants to determine the minimum number of scalar operations required to process the sequence.



Additional Constraint: It should display the optimal order of the Multiplication



Help Emily to complete the task

Input format :
The first line contains a single integer n, representing the number of dimensions in the array

The second line contains n integers, representing the dimensions of the matrices.

Output format :
The output prints the minimum scalar multiplications considering the given constraint.

and then it display the optimal order of the Multiplication



Refer to the sample output for formatting specifications.

Code constraints :
3 ≤ n ≤ 100

1 ≤ dimensions of matrices ≤ 500

# --------------------------------
Input 1 :
5
1 2 3 4 3
#-----
Output 1 :
30
(((M1M2)M3)M4)
# --------------------------------
Input 2 :
3
10 20 30
#-----
Output 2 :
6000
(M1M2)
"""

def matrixMult(p):
    n = len(p)

    dp = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i,j):
                cost = dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost 
                    s[i][j] = k

    return dp, s

def print_optimate(s,i,j):
    if i == j:
        return f"M{i}"
    else:
        left = print_optimate(s,i,s[i][j])
        right = print_optimate(s, s[i][j] + 1, j)
        return f"({left}{right})"

n = int(input())
p = list(map(int, input().split()))

dp, s = matrixMult(p)

print(dp[1][n-1])

print(print_optimate(s,1,n- 1))
