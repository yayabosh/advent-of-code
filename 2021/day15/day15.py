with open("day15/input.txt") as f:
    risk_levels = [[int(n) for n in line.strip()] for line in f]

# Part One
dp = [[0] * len(risk_levels[0]) for i in range(len(risk_levels))]

for i in range(1, len(risk_levels[0])):
    dp[0][i] = dp[0][i - 1] + risk_levels[0][i]

for i in range(1, len(risk_levels)):
    dp[i][0] = dp[i - 1][0] + risk_levels[i][0]

for i in range(1, len(risk_levels)):
    for j in range(1, len(risk_levels[0])):
        arrival_cost = min(dp[i - 1][j], dp[i][j - 1])
        dp[i][j] = arrival_cost + risk_levels[i][j]

print(dp[-1][-1])

# Part Two
# Implement Dijkstra's, too lazy to do it in Python right now :P
