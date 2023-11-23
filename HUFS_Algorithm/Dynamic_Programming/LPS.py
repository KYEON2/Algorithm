# 최장 회문 부수열 (Longest Palindrome Subsequence)
"""
영어 대문자로만 구성된 문자열이 입력으로 주어지면, 입력 문자열의 부수열 중에서 가장 긴 회문의 길이를 출력하는 프로그램
- 입력 문자열의 길이는 1이상 2,500이하이다.
- 전형적인 LCS스타일의 동적계획법으로 접근
"""
def LCS(X, Y):
    n, m = len(X), len(Y)
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] != Y[j-1]:  # 마지막 글자가 다르면
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            else:  # 마지막 글자가 같으면
                dp[i][j] = dp[i-1][j-1] + 1
    return dp[n][m]

x = input()
reversed_x = x[::-1]
y = reversed_x

solve = LCS(x, y)
print(solve)