# LCS (Longest Common Subsequence)
def LCS(X, Y):
  n, m = len(X), len(Y)
  dp = [[0]*(n+1) for i in range(m+1)] 
  
  for i in range(0, m+1):
    dp[0][i] = 0
  for j in range(0, n+1):
    dp[j][0] = 0
  
  for i in range(1, n+1):
    for j in range(1, m+1):
      if X[i] != Y[j]: # 마지막 글자가 다르면
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
      else: # 마지막 글자가 같으면
        dp[i][j] = dp[i-1][j-1] + 1
  return dp[n][m]

x = input()
y = input()

solve = LCS(x, y)
print(solve)