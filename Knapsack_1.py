capacity = 45
merchandises = [[4,6],[8,12],[3,4],[5,3],[9,7],[2,1],[3,3],[1,2],[5,7],[2,3],[4,4],[2,2],[7,10],[10,13],[3,5],[13,16],[11,14],[8,9]]

best_merchandices = []
best_price = 0
best_capacity = 0

current_merchandices = []
current_capacity = 0
current_price = 0

n = len(merchandises)

for bit in range(2 ** n):
    for i in range(n):
        if bit & (1 << i):
            current_capacity += merchandises[i][0]
            current_price += merchandises[i][1]
            current_merchandices.append(i+1)
    if (current_capacity <= capacity) and (current_price > best_price):
        best_price = current_price
        best_capacity = current_capacity
        best_merchandices = current_merchandices
    current_price = 0
    current_capacity = 0
    current_merchandices = []

print(best_price)
print(best_capacity)
print(best_merchandices)