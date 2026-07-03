capacity = 45
merchandises = [
    [4,6],[8,12],[3,4],[5,3],[9,7],[2,1],
    [3,3],[1,2],[5,7],[2,3],[4,4],[2,2],
    [7,10],[10,13],[3,5],[13,16],[11,14],[8,9]
]

n = len(merchandises)

# dp[i][w] = i個目までの商品を使って容量w以下で得られる最大価格
dp = [[0]*(capacity+1) for _ in range(n+1)]

for i in range(1, n+1):
    volume = merchandises[i-1][0]
    price = merchandises[i-1][1]

    for w in range(capacity+1):
        # 選ばない
        dp[i][w] = dp[i-1][w]

        # 選べるなら選ぶ場合も比較
        if volume <= w:
            dp[i][w] = max(
                dp[i][w],
                dp[i-1][w-volume] + price
            )

print("最大価格 =", dp[n][capacity])

selected = []

w = capacity

for i in range(n, 0, -1):
    if dp[i][w] != dp[i-1][w]:
        selected.append(i)
        w -= merchandises[i-1][0]

selected.reverse()

print("商品番号 =", selected)