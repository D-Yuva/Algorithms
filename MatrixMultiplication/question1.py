"""
Single File Programming Question
Problem Statement



Alice is tasked with solving the Matrix Chain Multiplication problem using a dynamic programming approach. Given a sequence of matrices and their dimensions, her aim is to determine the minimum number of scalar multiplications required to compute the matrix product.



The problem is to find the optimal order of matrix multiplication, as the order in which the matrices are multiplied affects the number of operations. 



Help Alice to complete the task

Input format :
The first line contains a single integer n, representing the number of dimensions in the array

The second line contains n integers,p[0],p[1],…,p[n−1], where p[i] represents the dimensions of the matrices.

Output format :
The output prints a single integer, the minimum number of scalar multiplications required to compute the product of the matrices in the optimal order.



Refer to the sample output for formatting specifications.

Code constraints :
3 ≤ n ≤ 100

1 ≤ p[i] ≤ 500
"""

# --------------------------------
# INPUT
# 5
# 30 35 15 5 10 20
#-----
# OUTPUT
# 15750
# --------------------------------

def matrix_chain_mult(p):
    n = len(p)

    dp = [[0] * (n) for _ in range(n)]

    for l in range(2,n+1):
        for i in range(1, n - l + 1):
            j = i + l - 1
            dp[i][j] = float("inf")
            for k in range(i,j):    
                cost = dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
            
    return dp[1][n-1]

n = int(input())
p = list(map(int, input().split()))
print(matrix_chain_mult(p))